# 🚀 Deploy to Vercel - Step by Step

## ✅ ขั้นที่ 1: เข้า Vercel

1. ไปที่ **https://vercel.com**
2. Click **"Sign Up"** (หรือ Login ถ้ามีบัญชี)
3. Select **"Continue with GitHub"**
4. Authorize Vercel

---

## ✅ ขั้นที่ 2: Import Project

1. Click **"Add New..."** → **"Project"**
2. Select **"Import an Existing Project"**
3. Paste GitHub URL:
   ```
   https://github.com/Hunsoul/mt5-license-api-vercel.git
   ```
4. Click **"Import"**

---

## ✅ ขั้นที่ 3: Configure Project

**Framework Preset:** Python (auto-detect)

**Root Directory:** `mt5-license-api-vercel/`

---

## ✅ ขั้นที่ 4: Environment Variables

Click **"Environment Variables"** และ add:

```
SUPABASE_URL = https://qbfhwvpgnbgjapkxrpqc.supabase.co
SUPABASE_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFiZmh3dnBnbmJnamFwa3hycHFjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzUxMDk2NjksImV4cCI6MjA1MDY4NTY2OX0.s-f9s4UR4VZnzVQvslZE9y_yp_wnxBbPJMzjXmrpGbY
SECRET_KEY = your-secret-key-change-in-production
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
```

---

## ✅ ขั้นที่ 5: Deploy!

Click **"Deploy"** แล้วรอ ~2-3 นาที

---

## ✅ ขั้นที่ 6: Verify

หลังสำเร็จ จะเห็น:
- **Production URL:** `https://mt5-license-api-vercel.vercel.app`
- **Test API:**
  ```bash
  curl https://mt5-license-api-vercel.vercel.app/api/health
  ```

---

## 📋 ตรวจสอบสถานะ

Vercel Dashboard:
- 🟢 **Production** = Ready to use
- 🔵 **Building** = กำลังสร้าง
- 🔴 **Failed** = มีปัญหา

---

## 🔗 API Endpoints (After Deploy)

```
Production:
https://mt5-license-api-vercel.vercel.app/api/license/activate
https://mt5-license-api-vercel.vercel.app/api/license/verify
https://mt5-license-api-vercel.vercel.app/api/health
```

---

## 🐛 Troubleshooting

**Deploy Failed?**
- Check build logs in Vercel dashboard
- Verify `.env` variables are set
- Ensure `vercel.json` is correct

**API Returns 404?**
- Wait ~5 minutes for cold start
- Check environment variables
- Verify Supabase connection

**Need to Update?**
- Make changes locally
- `git commit` + `git push`
- Vercel auto-deploys!

---

**ทำตามขั้นนี้เรียบร้อยแล้ว!** ✅
