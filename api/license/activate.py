from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api._utils import (
    supabase, get_client_ip, log_license_action, 
    parse_request_body, check_license_expiry
)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """
        Activate license with Account ID + HWID binding
        🔒 DOUBLE SECURITY LOCK
        """
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            data = parse_request_body(self.rfile, content_length)
            ip_address = get_client_ip(dict(self.headers))
            
            if not data:
                self._send_json(400, {'success': False, 'error': 'No data provided'})
                return
            
            license_key = data.get('license_key')
            account_id = data.get('account_id')
            hwid = data.get('hwid')
            
            # Validate required fields
            if not license_key:
                self._send_json(400, {'success': False, 'error': 'Missing license_key'})
                return
            if not account_id:
                self._send_json(400, {'success': False, 'error': 'Missing account_id'})
                return
            if not hwid:
                self._send_json(400, {'success': False, 'error': 'Missing hwid'})
                return
            
            # Convert account_id to string for consistency
            account_id = str(account_id)
            
            # Get license info
            result = supabase.table('licenses').select('*').eq('license_key', license_key).execute()
            
            if not result.data:
                log_license_action(license_key, account_id, 'ACTIVATION_FAILED_INVALID_KEY', ip_address)
                self._send_json(404, {'success': False, 'error': 'Invalid license key'})
                return
            
            license_data = result.data[0]
            
            # Check if license is active
            if not license_data.get('is_active', False):
                log_license_action(license_key, account_id, 'ACTIVATION_FAILED_INACTIVE', ip_address)
                self._send_json(403, {'success': False, 'error': 'License is inactive'})
                return
            
            # Check expiration
            if check_license_expiry(license_data.get('expires_at')):
                log_license_action(license_key, account_id, 'ACTIVATION_FAILED_EXPIRED', ip_address)
                self._send_json(403, {'success': False, 'error': 'License has expired'})
                return
            
            # 🔒 DOUBLE LOCK CHECK
            existing_account = license_data.get('account_id')
            existing_hwid = license_data.get('hwid')
            
            # Check 1: Account ID binding
            if existing_account and str(existing_account) != account_id:
                log_license_action(license_key, account_id, 'ACTIVATION_FAILED_DIFFERENT_ACCOUNT', ip_address, {
                    'bound_account': existing_account,
                    'attempted_account': account_id
                })
                self._send_json(403, {
                    'success': False,
                    'error': f'License already activated on different account (Account: {existing_account})'
                })
                return
            
            # Check 2: HWID binding
            if existing_hwid and existing_hwid != hwid:
                log_license_action(license_key, account_id, 'ACTIVATION_FAILED_DIFFERENT_MACHINE', ip_address, {
                    'bound_hwid': existing_hwid[:20] + '...',
                    'attempted_hwid': hwid[:20] + '...'
                })
                self._send_json(403, {
                    'success': False,
                    'error': 'License already activated on different machine. Contact admin to reset HWID.'
                })
                return
            
            # Check activation limit (only for new activations)
            current_activations = license_data.get('current_activations', 0)
            max_activations = license_data.get('max_activations', 1)
            
            if not existing_account and current_activations >= max_activations:
                log_license_action(license_key, account_id, 'ACTIVATION_FAILED_LIMIT_REACHED', ip_address)
                self._send_json(403, {'success': False, 'error': 'Maximum activations reached'})
                return
            
            # ✅ Activate license with DOUBLE BINDING
            update_data = {
                'account_id': account_id,
                'hwid': hwid,
                'last_used_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
            
            # Only increment if new activation
            if not existing_account:
                update_data['current_activations'] = current_activations + 1
            
            supabase.table('licenses').update(update_data).eq('license_key', license_key).execute()
            
            log_license_action(license_key, account_id, 'ACTIVATION_SUCCESS', ip_address, {
                'account_id': account_id,
                'hwid': hwid[:20] + '...'
            })
            
            self._send_json(200, {
                'success': True,
                'message': 'License activated successfully',
                'security': 'Account ID + HWID locked',
                'account_id': account_id,
                'expires_at': license_data.get('expires_at')
            })
            
        except Exception as e:
            print(f"Activation error: {str(e)}")
            self._send_json(500, {'success': False, 'error': 'Internal server error'})
    
    def _send_json(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
