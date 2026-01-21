from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timezone

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """API information endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'service': 'MT5 License API',
            'version': '3.0.0-vercel',
            'status': 'online',
            'security': 'JWT + Account ID + HWID (Double Lock)',
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'features': [
                'License activation with Account ID binding',
                'HWID machine binding (Double Lock)',
                'JWT authentication for admin',
                'HWID reset by admin',
                'Comprehensive logging'
            ],
            'endpoints': {
                'health': '/api/health [GET]',
                'auth_login': '/api/auth/login [POST]',
                'auth_verify': '/api/auth/verify [POST]',
                'activate': '/api/license/activate [POST]',
                'verify': '/api/license/verify [POST]',
                'deactivate': '/api/license/deactivate [POST]',
                'reset_hwid': '/api/license/reset-hwid [POST]'
            }
        }
        
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
