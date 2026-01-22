# 🎯 MT5 License Management System - Complete

**Full-stack license management platform with React-like dashboard, JWT authentication, HWID binding, and Vercel deployment.**

---

## 📋 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [License](#-license)

---

## ✨ Features

### Admin Dashboard
✅ License management (create, view, activate, deactivate)
✅ User management (create, edit, delete, roles)
✅ Activity logging (all admin actions tracked)
✅ License expiry alerts
✅ License request approvals
✅ Team management
✅ Settings management
✅ Export to CSV/Excel

### Security Features
🔐 JWT authentication with token expiry
🔐 Account ID + HWID double-lock binding
🔐 License activation/deactivation
🔐 HWID reset with change tracking
🔐 Rate limiting on API endpoints
🔐 CORS protection

### Backend Services
📧 Email notifications for expiry alerts
📅 Scheduled tasks (APScheduler)
📊 Activity logging to database
🔄 Real-time license status updates

### Deployment
🚀 Vercel serverless functions
🚀 Full static site hosting
🚀 Auto-scaling backend
🚀 Zero-cost infrastructure (within free tier)

---

## 🛠️ Tech Stack

### Frontend
- **HTML/CSS/JavaScript** - Pure vanilla (no framework)
- **Bootstrap 5.3.2** - UI framework
- **Chart.js 4.4.0** - Data visualization
- **Axios 1.6.0** - HTTP client
- **Supabase JS 2.x** - Database/auth client

### Backend
- **Python 3.13** - Runtime
- **Flask 3.0.0** - Web framework
- **PyJWT 2.10.1** - JWT tokens
- **Supabase SDK** - Database + Auth
- **APScheduler 3.10.4** - Background tasks
- **email-validator 2.1.0** - Email validation
- **python-dotenv** - Environment configuration

### Database
- **Supabase** (PostgreSQL)
- Tables: `licenses`, `users`, `license_logs`, `activity_logs`

### Deployment
- **Vercel** - Serverless platform
- **GitHub** - Version control
- **Docker** - Optional containerization

---

## 📁 Project Structure

```
mt5-license-api-v3-vercel/
├── api/                              # Vercel serverless functions
│   ├── license/
│   │   ├── activate.py              # Activate license with HWID
│   │   ├── verify.py                # Verify license validity
│   │   ├── deactivate.py            # Deactivate license
│   │   └── reset-hwid.py            # Reset HWID binding
│   ├── auth/
│   │   ├── login.py                 # Admin login
│   │   └── verify.py                # Token verification
│   ├── health.py                    # Health check endpoint
│   ├── index.py                     # Catch-all handler
│   ├── _utils.py                    # Shared utilities
│   ├── requirements.txt             # Python dependencies
│   └── vercel.json                  # Vercel config for api/
│
├── [Frontend Files]
│   ├── index.html                   # Dashboard home
│   ├── admin_login.html             # Login page
│   ├── licenses.html                # License management
│   ├── users.html                   # User management
│   ├── team.html                    # Team management
│   ├── dashboard.html               # Analytics dashboard
│   ├── approvals.html               # License approvals
│   ├── activity_logs.html           # Activity history
│   ├── expiry_alerts.html           # Expiry notifications
│   ├── settings.html                # Admin settings
│   ├── request_license.html         # License request form
│   ├── verify.html                  # API verification UI
│   ├── activity_logger.js           # Activity logging helper
│   ├── notification.js              # Notification system
│   └── api-client.js                # API integration layer
│
├── [Config Files]
│   ├── vercel.json                  # Vercel config (root)
│   ├── requirements.txt             # Python dependencies
│   ├── package.json                 # Frontend dependencies
│   ├── .env.example                 # Environment template
│   ├── .eslintrc.json               # JavaScript linting
│   ├── .prettierrc                  # Code formatter
│   ├── .gitignore                   # Git ignore rules
│   └── .pre-commit-config.yaml      # Pre-commit hooks
│
├── [Documentation]
│   ├── README.md                    # This file
│   ├── SETUP.md                     # Local setup guide
│   ├── DEPLOY_VERCEL.md             # Vercel deployment
│   ├── API_REFERENCE.md             # API documentation
│   └── LICENSE                      # MIT License
│
└── .git/                            # Git repository
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ 
- Python 3.8+
- Git
- GitHub account
- Vercel account (free tier)
- Supabase account (free tier)

### Local Development

```bash
# 1. Clone repository
git clone https://github.com/Hunsoul/mt5-license-api-vercel.git
cd mt5-license-api-vercel

# 2. Setup environment
cp .env.example .env
# Edit .env with your Supabase and SMTP credentials

# 3. Install dependencies
npm install
pip install -r requirements.txt

# 4. Run locally
python -m flask run              # Backend on :5000
npm run dev                       # Frontend dev server (optional)

# 5. Open browser
http://localhost:5000/admin_login.html
```

### Deployment to Vercel

**Automatic (Easiest):**
1. Go to https://vercel.com/new
2. Import this GitHub repository
3. Add environment variables
4. Click "Deploy"

**See:** [DEPLOY_VERCEL.md](./DEPLOY_VERCEL.md) for detailed steps

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login` | Login and get JWT token |
| POST | `/api/auth/verify` | Verify JWT token |

### License Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/license/activate` | Activate with Account ID + HWID |
| POST | `/api/license/verify` | Verify license validity |
| POST | `/api/license/deactivate` | Deactivate license |
| POST | `/api/license/reset-hwid` | Reset HWID binding |
| GET | `/api/health` | Health check |

### Example Requests

**Activate License:**
```bash
curl -X POST http://localhost:5000/api/license/activate \
  -H "Content-Type: application/json" \
  -d '{
    "license_key": "LIC-123456",
    "account_id": 12345,
    "hwid": "ABC123DEF456..."
  }'
```

**Verify License:**
```bash
curl -X POST http://localhost:5000/api/license/verify \
  -H "Content-Type: application/json" \
  -d '{
    "license_key": "LIC-123456",
    "hwid": "ABC123DEF456..."
  }'
```

---

## 🗄️ Database Schema

### `licenses` Table
```sql
CREATE TABLE licenses (
  id SERIAL PRIMARY KEY,
  license_key VARCHAR(50) UNIQUE NOT NULL,
  account_id INTEGER,
  hwid VARCHAR(255),
  is_active BOOLEAN DEFAULT true,
  expires_at TIMESTAMP,
  current_activations INTEGER DEFAULT 0,
  hwid_changes INTEGER DEFAULT 0,
  last_used_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### `users` Table
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  account_id INTEGER,
  email VARCHAR(255),
  full_name VARCHAR(255),
  line_id VARCHAR(100),
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### `license_logs` Table
```sql
CREATE TABLE license_logs (
  id SERIAL PRIMARY KEY,
  license_key VARCHAR(50),
  account_id INTEGER,
  action VARCHAR(50),
  ip_address VARCHAR(50),
  details JSONB,
  timestamp TIMESTAMP DEFAULT NOW()
);
```

### `activity_logs` Table
```sql
CREATE TABLE activity_logs (
  id SERIAL PRIMARY KEY,
  action VARCHAR(100),
  target_type VARCHAR(50),
  target_id VARCHAR(255),
  admin_id INTEGER,
  details JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🔧 Configuration

### Environment Variables (.env)

```env
# Supabase
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=eyJhbGciOi...

# JWT
SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Email (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password

# Flask
FLASK_ENV=production
FLASK_DEBUG=False
```

---

## 📚 Documentation

- **[SETUP.md](./SETUP.md)** - Complete local setup guide
- **[DEPLOY_VERCEL.md](./DEPLOY_VERCEL.md)** - Vercel deployment step-by-step
- **[API_REFERENCE.md](./verify.html)** - API endpoint documentation
- **[Activity Logger](./activity_logger.js)** - Usage examples in comments

---

## 🧪 Testing

### API Testing
Use the built-in [verify.html](./verify.html) page for interactive API testing.

### Local Testing
```bash
# Health check
curl http://localhost:5000/api/health

# With API client
# Include api-client.js in your HTML
// const result = await API.verifyLicense('key', 'hwid');
```

---

## 🚀 Deployment Checklist

- [ ] All environment variables set in Vercel
- [ ] Supabase project created and configured
- [ ] Database tables created
- [ ] API endpoints tested
- [ ] Frontend pages loading correctly
- [ ] Login working with JWT
- [ ] Email alerts configured
- [ ] CORS headers set
- [ ] Domain pointing to Vercel (optional)

---

## 🛡️ Security Notes

⚠️ **Important:**
- Never commit `.env` file
- Use strong `SECRET_KEY` (32+ chars)
- Rotate SMTP passwords monthly
- Enable Supabase RLS policies
- Monitor activity logs regularly
- Keep dependencies updated

---

## 🐛 Troubleshooting

### API Returns 500 Error
- Check environment variables in Vercel
- Review logs in Vercel dashboard
- Verify Supabase credentials
- Check database connection

### Frontend Not Loading
- Verify all routes in `vercel.json`
- Check static file MIME types
- Clear browser cache
- Test with incognito mode

### CORS Errors
- Already configured in `api/_utils.py`
- Add more origins if needed
- Check request headers

---

## 📄 License

MIT License - See [LICENSE](./LICENSE) file

---

## 👨‍💻 Author

Developed with ❤️ for MT5 License Management

**Repository:** https://github.com/Hunsoul/mt5-license-api-vercel

---

## 📞 Support

For issues and questions:
1. Check [SETUP.md](./SETUP.md) troubleshooting section
2. Review [DEPLOY_VERCEL.md](./DEPLOY_VERCEL.md) for deployment issues
3. Check Vercel logs: https://vercel.com/dashboard
4. Check Supabase logs and status

---

**Last Updated:** January 22, 2026
**Status:** ✅ Production Ready for Vercel Deployment
