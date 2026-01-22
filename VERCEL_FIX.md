# 🔧 Vercel Deployment Fix - Step by Step

## ⚠️ Problem
Build Failed: "The specified Root Directory "mt5-license-api-vercel" does not exist."

## ✅ Solution

### Method 1: Fix via Vercel Web Console (Easiest)

1. **Login to Vercel**: https://vercel.com/dashboard

2. **Select Project**: Click on `mt5-license-api-vercel`

3. **Go to Settings**:
   - Settings tab → General
   
4. **Update Root Directory**:
   - Find "Root Directory" field
   - Change from: `mt5-license-api-vercel`
   - Change to: `.` (just a dot)
   - Click "Save"

5. **Redeploy**:
   - Go to "Deployments" tab
   - Find the failed deployment
   - Click the "..." menu
   - Select "Redeploy"
   - Wait 2-5 minutes ✅

---

### Method 2: Fix via Vercel CLI (Advanced)

```bash
# 1. Login to Vercel
vercel login

# 2. Link project (if not linked)
cd D:\AdminPJ MM\mt5-license-api-v3-vercel
vercel link

# 3. Edit project settings
vercel project settings

# 4. Set Root Directory to "."
# When prompted for Root Directory: type "." and press Enter

# 5. Redeploy
vercel --prod
```

---

## 📋 Verification Checklist

After fixing and redeploying:

✅ Deployment shows "Ready" (green checkmark)
✅ No build errors in logs
✅ API endpoints accessible: `/api/health`
✅ Frontend loads: `/index.html`
✅ Database connection working

---

## 🐛 If Still Failing

### Check Build Logs:
1. Vercel Dashboard → Deployments
2. Click on the failed deployment
3. Scroll to "Build Logs"
4. Look for specific error messages

### Common Issues:
- **"requirements.txt not found"** → File must be in root
- **"Python version mismatch"** → Add `runtime.txt` with `python-3.11`
- **"Module not found"** → Check `api/_utils.py` imports

### Add runtime.txt (if needed):
Create file in root: `D:\AdminPJ MM\mt5-license-api-v3-vercel\runtime.txt`
```
python-3.11
```

---

## 🎯 Expected Result

After successful deployment:
- **Production URL**: `https://mt5-license-api-vercel-xxxxx.vercel.app`
- **API Base**: `https://mt5-license-api-vercel-xxxxx.vercel.app/api`
- **Frontend**: `https://mt5-license-api-vercel-xxxxx.vercel.app/index.html`

---

## 📞 Need Help?

1. Check [DEPLOY_VERCEL.md](./DEPLOY_VERCEL.md) for full guide
2. Review Vercel logs in dashboard
3. Verify GitHub repository is up-to-date
4. Try deleting deployment and redeploying from scratch

---

**Generated**: 2026-01-22
**Status**: Ready to fix
