@echo off
REM MT5 License API - GitHub Setup Script

echo.
echo ====================================
echo MT5 License API - GitHub Setup
echo ====================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git first.
    echo 📥 Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git found

REM Initialize git repository
if not exist .git (
    echo.
    echo 🔧 Initializing Git repository...
    git init
    
    echo.
    echo 👤 Configure Git user:
    set /p gitname="Enter your name: "
    set /p gitemail="Enter your email: "
    
    git config user.name "%gitname%"
    git config user.email "%gitemail%"
    
    echo ✅ Git initialized
) else (
    echo ✅ Git repository already exists
)

REM Add files
echo.
echo 📝 Adding files to Git...
git add .
echo ✅ Files added

REM Create initial commit
echo.
echo 💾 Creating initial commit...
git commit -m "🎉 Initial commit: MT5 License API with both Monolithic and Vercel Serverless versions"
echo ✅ Commit created

REM Add remote repository
echo.
echo 🔗 GitHub Repository Setup
echo.
echo To push to GitHub, you need to:
echo.
echo 1. Create a new repository on GitHub:
echo    👉 https://github.com/new
echo.
echo 2. Copy the repository URL (e.g., https://github.com/your-username/mt5-license-api.git)
echo.
set /p remoteurl="Enter GitHub repository URL: "

if not "%remoteurl%"=="" (
    git remote add origin %remoteurl%
    echo ✅ Remote repository added
    
    echo.
    echo 🚀 Pushing to GitHub...
    echo (This may prompt you to authenticate with GitHub)
    echo.
    
    git branch -M main
    git push -u origin main
    
    if errorlevel 0 (
        echo.
        echo ✅ Successfully pushed to GitHub!
        echo.
        echo 📍 Repository URL: %remoteurl%
        echo.
    ) else (
        echo.
        echo ⚠️ Push failed. Please check your GitHub URL and credentials.
        echo.
    )
) else (
    echo ⚠️ GitHub repository URL not provided.
    echo.
    echo To push later, run:
    echo   git remote add origin YOUR_GITHUB_URL
    echo   git push -u origin main
)

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.

pause
