# MT5 License API v3.0.0 - Vercel Serverless

## 🔐 Security Features

### Double Lock System
- **Lock 1:** Account ID (1 License = 1 MT5 Account)
- **Lock 2:** HWID (1 License = 1 Machine)

### Admin Features
- JWT Authentication
- Reset HWID for customers
- Activity logging

## 📡 Endpoints

### Public
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/api/health` | Health check |

### License (EA calls these)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/license/activate` | Activate with Account ID + HWID |
| POST | `/api/license/verify` | Verify license |
| POST | `/api/license/deactivate` | Deactivate license |

### Admin (requires JWT)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login` | Get JWT token |
| POST | `/api/auth/verify` | Verify JWT token |
| POST | `/api/license/reset-hwid` | Reset HWID (admin only) |

## 🚀 Deploy to Vercel

1. Push to GitHub
2. Connect to Vercel
3. Set Environment Variables:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `SECRET_KEY` (for JWT)
4. Deploy!

## ✅ Benefits

- **No Cold Start!** - Instant response every time
- **Free 1M requests/month** - Enough for 500+ users
- **Auto-scale** - Handle traffic spikes
- **99.99% uptime** - Reliable

## 📝 Request Examples

### Activate License
```json
POST /api/license/activate
{
  "license_key": "XXXX-XXXX-XXXX-XXXX",
  "account_id": "12345678",
  "hwid": "MACHINE-UNIQUE-ID"
}
```

### Verify License
```json
POST /api/license/verify
{
  "license_key": "XXXX-XXXX-XXXX-XXXX",
  "hwid": "MACHINE-UNIQUE-ID",
  "account_id": "12345678"  // optional
}
```

### Reset HWID (Admin)
```json
POST /api/license/reset-hwid
Authorization: Bearer <jwt_token>
{
  "license_key": "XXXX-XXXX-XXXX-XXXX"
}
```

## ⚔️ FOR THE EMPEROR!
