from http.server import BaseHTTPRequestHandler
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api._utils import verify_jwt, parse_request_body

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Verify JWT token"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            data = parse_request_body(self.rfile, content_length)
            
            if not data:
                self._send_json(400, {'success': False, 'error': 'No data provided'})
                return
            
            token = data.get('token')
            
            if not token:
                self._send_json(400, {'success': False, 'error': 'Token required'})
                return
            
            payload = verify_jwt(token)
            
            if not payload:
                self._send_json(401, {'success': False, 'error': 'Invalid or expired token'})
                return
            
            self._send_json(200, {
                'success': True,
                'user': {
                    'user_id': payload.get('user_id'),
                    'username': payload.get('username'),
                    'role': payload.get('role')
                }
            })
            
        except Exception as e:
            print(f"Token verification error: {str(e)}")
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
