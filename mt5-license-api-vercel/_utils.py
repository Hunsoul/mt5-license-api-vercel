# Shared utilities for all endpoints
import os
import json
from datetime import datetime, timezone, timedelta
from supabase import create_client, Client
import jwt

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://qbfhwvpgnbgjapkxrpqc.supabase.co')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFiZmh3dnBnbmJnamFwa3hycHFjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzUxMDk2NjksImV4cCI6MjA1MDY4NTY2OX0.s-f9s4UR4VZnzVQvslZE9y_yp_wnxBbPJMzjXmrpGbY')

# JWT Configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_HOURS = 24

# Initialize Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_client_ip(headers):
    """Get client IP address"""
    forwarded = headers.get('x-forwarded-for', '')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return headers.get('x-real-ip', 'unknown')

def log_license_action(license_key, account_id, action, ip_address, details=None):
    """Log license actions to database"""
    try:
        log_data = {
            'license_key': license_key,
            'account_id': str(account_id) if account_id else None,
            'action': action,
            'ip_address': ip_address,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        if details:
            log_data['details'] = json.dumps(details) if isinstance(details, dict) else str(details)
        supabase.table('license_logs').insert(log_data).execute()
    except Exception as e:
        print(f"Failed to log action: {str(e)}")

def generate_jwt(data):
    """Generate JWT token"""
    payload = {
        **data,
        'iat': datetime.now(timezone.utc),
        'exp': datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRATION_HOURS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)

def verify_jwt(token):
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def parse_request_body(rfile, content_length):
    """Parse JSON request body"""
    try:
        if content_length > 0:
            body = rfile.read(content_length)
            return json.loads(body)
        return {}
    except:
        return {}

def check_license_expiry(expires_at):
    """Check if license has expired"""
    if not expires_at:
        return False  # No expiry = lifetime
    try:
        expiry = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
        return expiry < datetime.now(timezone.utc)
    except:
        return False

def calculate_days_remaining(expires_at):
    """Calculate days remaining until expiry"""
    if not expires_at:
        return None  # Lifetime license
    try:
        expiry = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
        return (expiry - datetime.now(timezone.utc)).days
    except:
        return None
