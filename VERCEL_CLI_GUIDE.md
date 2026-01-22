# 🚀 Vercel CLI Deployment - Simplified Steps

## Step 1: Generate Vercel Token (Web)

1. Go to: https://vercel.com/account/tokens
2. Click "Create Token"
3. Name: `mt5-license-api-deploy`
4. Copy the token (it appears once!)
5. Save somewhere safe temporarily

---

## Step 2: Use Token to Deploy

Open PowerShell in `D:\AdminPJ MM\mt5-license-api-v3-vercel` and run:

```powershell
# Set token as environment variable
$env:VERCEL_TOKEN = "YOUR_TOKEN_HERE"

# Login with token
vercel login --token $env:VERCEL_TOKEN

# Link project (if not already linked)
vercel link --yes

# Deploy to production
vercel --prod
```

### Or use one-liner:

```powershell
$env:VERCEL_TOKEN = "YOUR_TOKEN_HERE"; vercel login --token $env:VERCEL_TOKEN; vercel link --yes; vercel --prod
```

---

## Step 3: Fix Root Directory (if needed)

If deployment still fails with "Root Directory" error:

```powershell
# Open project settings
vercel project settings

# When prompted for Root Directory, enter: .
```

Then redeploy:
```powershell
vercel --prod
```

---

## Step 4: Verify

After successful deployment:

```powershell
# Check deployment URL
vercel ls

# Test API
curl https://your-vercel-url.vercel.app/api/health
```

---

## Alternative: Use Web Console

If CLI is too complex, just use:
1. https://vercel.com/dashboard
2. Find your project
3. Go to Settings → General
4. Set Root Directory to `.`
5. Redeploy from Deployments tab

---

**Note**: Token will be shown only once. If you lose it, generate a new one.
