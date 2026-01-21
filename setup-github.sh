#!/bin/bash

# MT5 License API - GitHub Setup Script

echo ""
echo "===================================="
echo "MT5 License API - GitHub Setup"
echo "===================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    echo "📥 Download from: https://git-scm.com/download/linux"
    exit 1
fi

echo "✅ Git found"

# Initialize git repository
if [ ! -d .git ]; then
    echo ""
    echo "🔧 Initializing Git repository..."
    git init
    
    echo ""
    echo "👤 Configure Git user:"
    read -p "Enter your name: " gitname
    read -p "Enter your email: " gitemail
    
    git config user.name "$gitname"
    git config user.email "$gitemail"
    
    echo "✅ Git initialized"
else
    echo "✅ Git repository already exists"
fi

# Add files
echo ""
echo "📝 Adding files to Git..."
git add .
echo "✅ Files added"

# Create initial commit
echo ""
echo "💾 Creating initial commit..."
git commit -m "🎉 Initial commit: MT5 License API with both Monolithic and Vercel Serverless versions"
echo "✅ Commit created"

# Add remote repository
echo ""
echo "🔗 GitHub Repository Setup"
echo ""
echo "To push to GitHub, you need to:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   👉 https://github.com/new"
echo ""
echo "2. Copy the repository URL (e.g., https://github.com/your-username/mt5-license-api.git)"
echo ""
read -p "Enter GitHub repository URL: " remoteurl

if [ ! -z "$remoteurl" ]; then
    git remote add origin "$remoteurl"
    echo "✅ Remote repository added"
    
    echo ""
    echo "🚀 Pushing to GitHub..."
    echo "(This may prompt you to authenticate with GitHub)"
    echo ""
    
    git branch -M main
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Successfully pushed to GitHub!"
        echo ""
        echo "📍 Repository URL: $remoteurl"
        echo ""
    else
        echo ""
        echo "⚠️ Push failed. Please check your GitHub URL and credentials."
        echo ""
    fi
else
    echo "⚠️ GitHub repository URL not provided."
    echo ""
    echo "To push later, run:"
    echo "  git remote add origin YOUR_GITHUB_URL"
    echo "  git push -u origin main"
fi

echo ""
echo "===================================="
echo "Setup Complete!"
echo "===================================="
echo ""
