# MT5 License Management System 🔐

**Advanced License Management API for MT5** with support for both traditional serverful and serverless deployments.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask 3.0](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)

## 🎯 Features

### 🔒 Security
- **Double Lock System** - Account ID + HWID binding
- **JWT Authentication** - Secure admin access
- **Rate Limiting** - Prevent abuse
- **CORS Protection** - Secure cross-origin requests
- **Activity Logging** - Audit trail of all actions

### 📧 Notifications
- **Email Alerts** - Automatic expiry notifications (7 days before)
- **Background Scheduler** - 24/7 monitoring
- **Configurable SMTP** - Any email provider

### 🚀 Deployment Options
- **Monolithic** (`mt5-license-api/`) - VPS, Docker, Cloud VM
- **Serverless** (`mt5-license-api-vercel/`) - Vercel, AWS Lambda, Google Cloud Functions

## 📁 Project Structure

```
├── mt5-license-api/                 # Monolithic version (Flask)
│   ├── app.py                       # Main Flask application
│   ├── requirements.txt             # Python dependencies
│   └── Dockerfile                   # Docker configuration
│
├── mt5-license-api-vercel/          # Serverless version (Vercel)
│   ├── api/
│   │   ├── index.py                 # Main entry point
│   │   ├── health.py                # Health check
│   │   ├── _utils.py                # Utility functions
│   │   ├── auth/                    # Authentication endpoints
│   │   │   ├── login.py
│   │   │   └── verify.py
│   │   └── license/                 # License endpoints
│   │       ├── activate.py
│   │       ├── verify.py
│   │       ├── deactivate.py
│   │       └── reset-hwid.py
│   ├── requirements.txt
│   ├── vercel.json                  # Vercel configuration
│   └── README.md
│
├── package.json                     # Frontend dependencies
├── .env.example                     # Environment template
├── docker-compose.yml               # Docker compose
├── SETUP.md                         # Setup guide
└── README.md                        # This file
```

## 🚀 Quick Start

### Option 1: Monolithic (Traditional)

```bash
# 1. Install dependencies
cd mt5-license-api
pip install -r requirements.txt

# 2. Configure environment
cp ../.env.example .env
# Edit .env with your settings

# 3. Run
python app.py
# API available at http://localhost:5000
```

### Option 2: Serverless (Vercel)

```bash
# 1. Install dependencies
cd mt5-license-api-vercel
pip install -r requirements.txt

# 2. Deploy to Vercel
vercel

# 3. Set environment variables in Vercel dashboard
```

### Option 3: Docker

```bash
# 1. Build and run everything
docker-compose up

# 2. API available at http://localhost:5000
# Frontend available at http://localhost:8000
```

## 📡 API Endpoints

### Public Endpoints
```
GET  /                          # API information
GET  /api/health                # Health check
POST /api/license/activate      # Activate license with HWID
POST /api/license/verify        # Verify license validity
POST /api/license/deactivate    # Deactivate license
```

### Admin Endpoints (JWT required)
```
POST /api/auth/login            # Get JWT token
POST /api/auth/verify           # Verify token
POST /api/license/reset-hwid    # Reset HWID (admin only)
```

## 🔐 Usage Example

### 1. Activate License
```bash
curl -X POST http://localhost:5000/api/license/activate \
  -H "Content-Type: application/json" \
  -d '{
    "license_key": "LIC-123456",
    "account_id": "user@example.com",
    "hwid": "ABC-123-XYZ"
  }'
```

### 2. Verify License
```bash
curl -X POST http://localhost:5000/api/license/verify \
  -H "Content-Type: application/json" \
  -d '{
    "license_key": "LIC-123456",
    "hwid": "ABC-123-XYZ"
  }'
```

### 3. Admin Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "password"
  }'
```

## 🔧 Configuration

### Environment Variables

**Required:**
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SECRET_KEY=your-secret-key-change-in-production
```

**Optional (Email Alerts):**
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
```

See [.env.example](.env.example) for all available options.

## 📚 Documentation

- **[Setup Guide](SETUP.md)** - Detailed installation and configuration
- **[API Documentation](mt5-license-api/README.md)** - Full endpoint reference
- **[Vercel Deployment](mt5-license-api-vercel/README.md)** - Serverless deployment guide

## 🛠️ Technologies Used

### Backend
- **Flask 3.0** - Web framework
- **Supabase** - Database & authentication
- **PyJWT** - JWT tokens
- **APScheduler** - Background tasks
- **Flask-Limiter** - Rate limiting
- **Gunicorn** - Production server

### Frontend
- **Vanilla JavaScript** - No framework overhead
- **Bootstrap 5** - UI framework
- **Chart.js** - Data visualization
- **Axios** - HTTP client

### DevOps
- **Docker** - Containerization
- **Vercel** - Serverless platform
- **GitHub** - Version control

## 📊 Performance

### Monolithic Version
- ⚡ Response time: ~50-100ms (local), ~150-300ms (cloud)
- 💾 Memory: ~50-100MB
- 🔄 Concurrent users: 100+ (depends on hosting)

### Serverless Version
- ⚡ Response time: ~50-100ms (cold start after 15 mins: ~500ms)
- 💾 Memory: On-demand
- 🔄 Concurrent users: Unlimited (auto-scaling)

## 💰 Pricing

### Monolithic
- Hosting: $5-20/month (VPS) or your existing infrastructure
- Database: Supabase free tier includes 500MB

### Serverless
- **Free tier**: 1M requests/month (enough for 500+ users)
- **Overages**: $0.50 per 100K requests
- **Database**: Supabase free tier

## 🔐 Security Considerations

1. **Change SECRET_KEY** - Generate a strong random key in production
2. **Use HTTPS** - Always use HTTPS in production
3. **Update Dependencies** - Regularly update packages
4. **Rate Limiting** - Enabled by default
5. **CORS Configuration** - Configure allowed origins

## 📈 Scalability

### Monolithic
- Scale vertically (more powerful server)
- Or deploy multiple instances with load balancer

### Serverless
- Auto-scales automatically
- Unlimited concurrent requests
- Pay only for what you use

## 🐛 Troubleshooting

### Cold Start Issues
- **Monolithic**: Pre-warm application with periodic requests
- **Serverless**: Normal behavior, first request after 15 mins idle takes ~500ms

### Email Not Sending
- Verify SMTP credentials in `.env`
- Check email provider (Gmail requires app password)
- Check spam folder

### Database Connection Errors
- Verify Supabase URL and key
- Check network connectivity
- Verify database tables exist

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ for MT5 license management**
