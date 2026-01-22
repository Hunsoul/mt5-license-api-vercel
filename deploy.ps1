#!/usr/bin/env pwsh
# Vercel Deployment Script - PowerShell Version

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   MT5 License API - Vercel Deploy" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verify directory
if (!(Test-Path "vercel.json")) {
    Write-Host "ERROR: vercel.json not found!" -ForegroundColor Red
    Write-Host "Make sure you're in: D:\AdminPJ MM\mt5-license-api-v3-vercel" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

$vercelCmd = "C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd"

# Check Vercel
Write-Host "[1/4] Checking Vercel CLI..." -ForegroundColor Green
& $vercelCmd --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Vercel CLI failed" -ForegroundColor Red
    exit 1
}

# Step 1: Login
Write-Host ""
Write-Host "[2/4] Login to Vercel..." -ForegroundColor Green
Write-Host "Instructions will appear in browser" -ForegroundColor Yellow
& $vercelCmd login

# Step 2: Link Project
Write-Host ""
Write-Host "[3/4] Linking project to Vercel..." -ForegroundColor Green
Write-Host "Select or create new project" -ForegroundColor Yellow
& $vercelCmd link

# Step 3: Deploy
Write-Host ""
Write-Host "[4/4] Deploying to production..." -ForegroundColor Green
& $vercelCmd --prod

Write-Host ""
Write-Host "✅ Deployment complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Check your production URL above" -ForegroundColor White
Write-Host "2. Test API: https://your-url.app/api/health" -ForegroundColor White
Write-Host "3. Update api-client.js baseURL if needed" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to exit"
