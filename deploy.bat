@echo off
REM Vercel Deployment Script for mt5-license-api-vercel

echo.
echo ========================================
echo   MT5 License API - Vercel Deployment
echo ========================================
echo.

REM Step 1: Verify we're in the right directory
if not exist "vercel.json" (
    echo ERROR: vercel.json not found!
    echo Make sure you're in: D:\AdminPJ MM\mt5-license-api-v3-vercel
    pause
    exit /b 1
)

echo [1/5] Checking Vercel CLI...
call "C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd" --version
if errorlevel 1 (
    echo ERROR: Vercel CLI not installed
    pause
    exit /b 1
)

echo.
echo [2/5] Linking to Vercel project...
echo NOTE: You may need to authenticate with GitHub
call "C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd" link

echo.
echo [3/5] Setting Root Directory to '.' ...
REM Note: Interactive config done via vercel project settings
echo NOTE: If prompted, set Root Directory to: .
echo (just a single dot)

echo.
echo [4/5] Deploying to production...
call "C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd" --prod

echo.
echo [5/5] Done!
echo.
echo Your deployment URL should be displayed above.
echo Test with: https://your-vercel-url.app/api/health
echo.
pause
