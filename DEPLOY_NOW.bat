@echo off
cd /d "D:\AdminPJ MM\mt5-license-api-v3-vercel"
echo.
echo ===================================
echo    MT5 License API - Vercel Deploy
echo ===================================
echo.
echo Step 1: Login with Vercel
echo Browser will open for authentication
echo.
call C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd login
if errorlevel 1 goto error

echo.
echo Step 2: Link to Vercel Project
echo Select project or create new one
echo.
call C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd link
if errorlevel 1 goto error

echo.
echo Step 3: Deploy to Production
echo Please wait...
echo.
call C:\Users\ttoon\AppData\Roaming\npm\vercel.cmd --prod
if errorlevel 1 goto error

echo.
echo.
echo ===================================
echo   SUCCESS! Deployment Complete
echo ===================================
echo.
echo Your production URL is shown above.
echo Test with: https://your-url.vercel.app/api/health
echo.
pause
exit /b 0

:error
echo.
echo ERROR: Deployment failed!
echo.
pause
exit /b 1
