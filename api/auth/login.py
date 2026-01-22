from http.server import BaseHTTPRequestHandler
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api._utils import supabase, generate_jwt, parse_request_body

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Login endpoint - returns JWT token"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            data = parse_request_body(self.rfile, content_length)
            
            if not data:
                self._send_json(400, {'success': False, 'error': 'No data provided'})
                return
            
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                self._send_json(400, {'success': False, 'error': 'Missing username or password'})
                return
            
            # Authenticate against admin users
            result = supabase.table('admin_users').select('*').eq('username', username).execute()
            
            if not result.data:
                self._send_json(401, {'success': False, 'error': 'Invalid credentials'})
                return
            
            admin_user = result.data[0]
            
            # Check password (in production, use bcrypt)
            if admin_user.get('password') != password:
                self._send_json(401, {'success': False, 'error': 'Invalid credentials'})
                return
            
            # Generate JWT token
            token = generate_jwt({
                'user_id': admin_user['id'],
                'username': admin_user['username'],
                'role': admin_user.get('role', 'user')
            })
            
            self._send_json(200, {
                'success': True,
                'token': token,
                'user': {
                    'id': admin_user['id'],
                    'username': admin_user['username'],
                    'role': admin_user.get('role', 'user')
                }
            })
            
        except Exception as e:
            print(f"Login error: {str(e)}")
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
