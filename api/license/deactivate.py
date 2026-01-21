from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api._utils import (
    supabase, get_client_ip, log_license_action, parse_request_body
)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """
        Deactivate license (unbind from account and machine)
        """
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            data = parse_request_body(self.rfile, content_length)
            ip_address = get_client_ip(dict(self.headers))
            
            if not data:
                self._send_json(400, {'success': False, 'error': 'No data provided'})
                return
            
            license_key = data.get('license_key')
            
            if not license_key:
                self._send_json(400, {'success': False, 'error': 'Missing license_key'})
                return
            
            # Get license info
            result = supabase.table('licenses').select('*').eq('license_key', license_key).execute()
            
            if not result.data:
                self._send_json(404, {'success': False, 'error': 'Invalid license key'})
                return
            
            license_data = result.data[0]
            
            # Store previous values for logging
            previous_account = license_data.get('account_id')
            previous_hwid = license_data.get('hwid')
            
            # Deactivate - Clear both account_id and hwid
            current_activations = license_data.get('current_activations', 1)
            update_data = {
                'account_id': None,
                'hwid': None,
                'current_activations': max(0, current_activations - 1),
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
            
            supabase.table('licenses').update(update_data).eq('license_key', license_key).execute()
            
            log_license_action(license_key, previous_account, 'DEACTIVATION_SUCCESS', ip_address, {
                'previous_account': previous_account,
                'previous_hwid': previous_hwid[:20] + '...' if previous_hwid else None
            })
            
            self._send_json(200, {
                'success': True,
                'message': 'License deactivated successfully. Can be activated on new machine.'
            })
            
        except Exception as e:
            print(f"Deactivation error: {str(e)}")
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
