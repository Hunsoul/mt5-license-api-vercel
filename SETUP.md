# MT5 License Management System - Setup Guide

## ติดตั้ง

### 1. Backend (Python)
```bash
cd mt5-license-api
pip install -r requirements.txt
python app.py
```

### 2. Frontend (Node.js)
```bash
npm install
npm start
```

## สิ่งที่ติดตั้ง

### Python Packages
- **Flask** - Web Framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Supabase** - Database
- **Gunicorn** - Production Server
- **PyJWT** - JWT Authentication
- **APScheduler** - Background Task Scheduler
- **python-dotenv** - Environment Variables
- **pytest** - Testing Framework
- **black** - Code Formatter
- **flake8** - Code Linter
- **flask-limiter** - Rate Limiting
- **Flask-Talisman** - Security Headers
- **Flasgger** - Auto Swagger Documentation
- **email-validator** - Email Validation

### JavaScript Dependencies
- **Axios** - HTTP Client
- **Chart.js** - Charts & Graphs
- **Bootstrap** - UI Framework
- **SweetAlert2** - Beautiful Alerts
- **Moment.js** - Date Handling
- **Tailwind CSS** - Utility CSS Framework

### Dev Tools
- **prettier** - Code Formatter
- **eslint** - Code Linter

## วิธีใช้

### Format Code (Python)
```bash
black mt5-license-api/
```

### Lint Code (Python)
```bash
flake8 mt5-license-api/
```

### Run Tests (Python)
```bash
pytest
```

### Format Code (JavaScript)
```bash
npx prettier --write .
```

### Lint Code (JavaScript)
```bash
npx eslint .
```

## Features

### 🔐 Security
- JWT Authentication
- Account ID binding
- HWID (Hardware ID) machine binding
- Secure logging of all actions
- Rate limiting
- Security headers (CORS, CSP, etc.)

### 📧 Email Notifications
- Automatic expiry alerts (7 days before expiration)
- Configurable SMTP server
- HTML email templates

### ⏰ Background Tasks
- Automatic license expiry checking (every 24 hours)
- Email notifications for expiring licenses
- Extensible task scheduler

### 📊 Monitoring
- Health check endpoint
- Comprehensive audit logs
- Database connection testing
- Scheduler status monitoring

## API Endpoints

### Authentication
- `POST /api/auth/login` - Login and get JWT token
- `POST /api/auth/verify` - Verify JWT token

### License Management
- `GET /api/health` - Health check
- `POST /api/license/activate` - Activate license with HWID binding
- `POST /api/license/verify` - Verify license validity
- `POST /api/license/deactivate` - Deactivate license
- `POST /api/license/reset-hwid` - Reset HWID (admin only)
- `GET /api/license/info` - Get license details

## Environment Variables
Create `.env` file and copy from `.env.example`

```env
# Required
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
SECRET_KEY=your-secret-key

# Optional - Email alerts
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
```

## Deployment

### Docker
```bash
docker-compose up
```

### Manual
```bash
# Terminal 1 - Backend
cd mt5-license-api
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app

# Terminal 2 - Frontend
npm start
```

## Default Ports
- API Server: http://localhost:5000
- Frontend: http://localhost:8000
- Swagger Docs: http://localhost:5000/apidocs
