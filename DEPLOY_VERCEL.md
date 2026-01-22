# 🚀 Vercel Deployment Guide - Complete

## Phase 1: Web Console Deployment

### Step 1: Go to Vercel Console
1. Open https://vercel.com/new
2. Login with your GitHub account
3. Click "Import GitHub Repository"

### Step 2: Select Repository
- Search for: `mt5-license-api-vercel`
- Select the repository
- Click "Import"

### Step 3: Configure Project Settings
- **Project Name**: `mt5-license-api-vercel` (or your preferred name)
- **Framework**: Select "Other" (since we have custom Python + HTML)
- **Root Directory**: Leave empty (default is root)
- **Build Command**: Leave empty
- **Output Directory**: Leave empty
- **Environment Variables**: Add ALL of these:

```
SUPABASE_URL=https://qbfhwvpgnbgjapkxrpqc.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SECRET_KEY=[CHANGE THIS - use a strong random string]
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
```

### Step 4: Click Deploy
- Click the "Deploy" button
- Wait for deployment to complete (2-5 minutes)
- You'll get a URL like: `https://mt5-license-api-vercel-xxxxx.vercel.app`

---

## Phase 2: Production Configuration

### Update Environment Variables in Vercel Console
1. Go to your project: `https://vercel.com/dashboard/projects`
2. Select `mt5-license-api-vercel`
3. Go to **Settings** → **Environment Variables**
4. Update these with production values:

| Variable | Value | Notes |
|----------|-------|-------|
| `SUPABASE_URL` | Your actual URL | From Supabase dashboard |
| `SUPABASE_KEY` | Your actual key | From Supabase dashboard |
| `SECRET_KEY` | Generate new | `openssl rand -hex 32` |
| `SMTP_SERVER` | smtp.gmail.com | For Gmail |
| `SMTP_PORT` | 587 | Standard TLS |
| `SENDER_EMAIL` | your@gmail.com | Gmail address |
| `SENDER_PASSWORD` | App password | Google App Password |

### Redeploy with New Variables
1. In Vercel console, go to **Deployments**
2. Find latest deployment
3. Click "..." → "Redeploy"

---

## Phase 3: Testing Deployment

### Test API Endpoints
```bash
# Health check
curl https://[YOUR-VERCEL-URL]/api/health

# Verify license (test)
curl -X POST https://[YOUR-VERCEL-URL]/api/license/verify \
  -H "Content-Type: application/json" \
  -d '{"license_key":"test-key","hwid":"test-hwid"}'

# Login (test)
curl -X POST https://[YOUR-VERCEL-URL]/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"password"}'
```

### Test Frontend
Open in browser: `https://[YOUR-VERCEL-URL]/index.html`

---

## Phase 4: Update Frontend API Base URL

If your API URL is different from `http://localhost:3000/api`, update in **api-client.js**:

```javascript
const API = {
    baseURL: 'https://[YOUR-VERCEL-URL]/api',  // ← Change this
    // ... rest of code
};
```

Then push to GitHub and redeploy.

---

## Troubleshooting

### Build Fails
- Check `vercel.json` syntax
- Ensure `requirements.txt` is in root or `api/`
- Check Python version compatibility

### Environment Variables Not Working
- Redeploy after adding variables
- Check variable names match exactly
- Use "Redeploy" button, not automatic deploy

### CORS Errors
- Add `Access-Control-Allow-Origin` headers in Flask
- Already configured in `api/_utils.py`

### Database Connection Failed
- Verify `SUPABASE_URL` and `SUPABASE_KEY` are correct
- Check Supabase project is active
- Test connection locally first

---

## Production Checklist

- [ ] Vercel project created and deployed
- [ ] All environment variables set
- [ ] API endpoints responding with 200/appropriate status
- [ ] Frontend loading on Vercel domain
- [ ] Database connection working
- [ ] Email notifications configured
- [ ] JWT tokens working
- [ ] CORS headers correct

---

## Important Notes

⚠️ **Security:**
- Never commit `.env` file to GitHub
- Use strong `SECRET_KEY` in production
- Rotate SMTP passwords regularly
- Use HTTPS only (Vercel default)

🔄 **Updates:**
- Push changes to GitHub
- Vercel auto-redeploys on push
- Check deployment logs if something fails

📊 **Monitoring:**
- Check logs: Vercel Dashboard → Project → Deployments → Logs
- Monitor errors in serverless functions
- Use Supabase dashboard for database issues

---

Generated: 2026-01-22
Status: Ready for Vercel deployment
