from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api._utils import (
    supabase, get_client_ip, log_license_action,
    parse_request_body, check_license_expiry, calculate_days_remaining
)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """
        Verify license with Account ID + HWID check
        🔒 DOUBLE SECURITY VERIFICATION
        """
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            data = parse_request_body(self.rfile, content_length)
            ip_address = get_client_ip(dict(self.headers))
            
            if not data:
                self._send_json(400, {'success': False, 'error': 'No data provided'})
                return
            
            license_key = data.get('license_key')
            hwid = data.get('hwid')
            account_id = data.get('account_id')  # Optional but recommended
            
            # Validate required fields
            if not license_key:
                self._send_json(400, {'success': False, 'error': 'Missing license_key'})
                return
            if not hwid:
                self._send_json(400, {'success': False, 'error': 'Missing hwid'})
                return
            
            # Get license info
            result = supabase.table('licenses').select('*').eq('license_key', license_key).execute()
            
            if not result.data:
                self._send_json(404, {'success': False, 'error': 'Invalid license key'})
                return
            
            license_data = result.data[0]
            
            # Check if license is active
            if not license_data.get('is_active', False):
                self._send_json(403, {'success': False, 'error': 'License is inactive'})
                return
            
            # Check expiration
            if check_license_expiry(license_data.get('expires_at')):
                self._send_json(403, {'success': False, 'error': 'License has expired'})
                return
            
            # 🔒 DOUBLE LOCK VERIFICATION
            
            # Check 1: License must be activated first
            if not license_data.get('hwid'):
                self._send_json(403, {
                    'success': False,
                    'error': 'License not activated. Please activate first.'
                })
                return
            
            # Check 2: HWID must match
            if license_data.get('hwid') != hwid:
                log_license_action(license_key, license_data.get('account_id'), 
                    'VERIFICATION_FAILED_WRONG_MACHINE', ip_address, {
                        'expected_hwid': license_data.get('hwid', '')[:20] + '...',
                        'provided_hwid': hwid[:20] + '...'
                    })
                self._send_json(403, {
                    'success': False,
                    'error': 'License is locked to different machine. Contact admin to reset HWID.'
                })
                return
            
            # Check 3: Account ID (if provided)
            if account_id and license_data.get('account_id'):
                if str(license_data.get('account_id')) != str(account_id):
                    log_license_action(license_key, account_id,
                        'VERIFICATION_FAILED_WRONG_ACCOUNT', ip_address, {
                            'expected_account': license_data.get('account_id'),
                            'provided_account': account_id
                        })
                    self._send_json(403, {
                        'success': False,
                        'error': f'License is locked to different account (Account: {license_data.get("account_id")})'
                    })
                    return
            
            # ✅ All checks passed - Update last used
            supabase.table('licenses').update({
                'last_used_at': datetime.now(timezone.utc).isoformat()
            }).eq('license_key', license_key).execute()
            
            log_license_action(license_key, license_data.get('account_id'), 
                'VERIFICATION_SUCCESS', ip_address)
            
            # Calculate days remaining
            days_remaining = calculate_days_remaining(license_data.get('expires_at'))
            
            self._send_json(200, {
                'success': True,
                'valid': True,
                'message': 'License is valid',
                'security': 'Account ID + HWID verified',
                'account_id': license_data.get('account_id'),
                'expires_at': license_data.get('expires_at'),
                'days_remaining': days_remaining,
                'is_active': license_data.get('is_active', True)
            })
            
        except Exception as e:
            print(f"Verification error: {str(e)}")
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
