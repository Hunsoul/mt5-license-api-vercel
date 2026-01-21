from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api._utils import (
    supabase, get_client_ip, log_license_action, 
    parse_request_body, verify_jwt
)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """
        Reset HWID for a license (Admin only)
        Requires JWT token with admin role
        """
        try:
            # Check authorization
            auth_header = self.headers.get('Authorization', '')
            if not auth_header.startswith('Bearer '):
                self._send_json(401, {'success': False, 'error': 'Authorization required'})
                return
            
            token = auth_header.split(' ')[1]
            payload = verify_jwt(token)
            
            if not payload:
                self._send_json(401, {'success': False, 'error': 'Invalid or expired token'})
                return
            
            # Check admin role
            if payload.get('role') != 'admin':
                self._send_json(403, {'success': False, 'error': 'Admin access required'})
                return
            
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
            previous_hwid = license_data.get('hwid')
            
            # Reset HWID only (keep account_id)
            hwid_changes = (license_data.get('hwid_changes') or 0) + 1
            update_data = {
                'hwid': None,
                'hwid_changes': hwid_changes,
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
            
            supabase.table('licenses').update(update_data).eq('license_key', license_key).execute()
            
            log_license_action(license_key, license_data.get('account_id'), 'HWID_RESET', ip_address, {
                'admin': payload.get('username'),
                'previous_hwid': previous_hwid[:20] + '...' if previous_hwid else None,
                'hwid_changes': hwid_changes
            })
            
            self._send_json(200, {
                'success': True,
                'message': 'HWID reset successfully. User can now activate on new machine.',
                'hwid_changes': hwid_changes
            })
            
        except Exception as e:
            print(f"HWID reset error: {str(e)}")
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
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
