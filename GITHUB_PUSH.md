# GitHub Push Guide

## 🚀 Push to GitHub in 3 Steps

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: `mt5-license-api`
3. Choose visibility (Public/Private)
4. Click "Create repository"
5. Copy the repository URL

### Step 2: Run Setup Script

**On Windows:**
```bash
./setup-github.bat
```

**On Mac/Linux:**
```bash
chmod +x setup-github.sh
./setup-github.sh
```

**Or Manual:**
```bash
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add .
git commit -m "🎉 Initial commit: MT5 License API"
git branch -M main
git remote add origin https://github.com/your-username/mt5-license-api.git
git push -u origin main
```

### Step 3: Verify on GitHub

Visit your repository URL and confirm all files are uploaded!

---

## 📁 What Gets Pushed

✅ **Source Code**
- `mt5-license-api/` - Monolithic Flask API
- `mt5-license-api-vercel/` - Serverless Vercel version
- Frontend HTML files

✅ **Configuration**
- `.env.example` - Environment template
- `docker-compose.yml` - Docker setup
- `vercel.json` - Vercel config
- `.prettierrc` - Code formatter config
- `.eslintrc.json` - JavaScript linter config

✅ **Documentation**
- `README.md` - Main documentation
- `SETUP.md` - Setup guide
- `GITHUB_PUSH.md` - This file

❌ **Ignored** (won't be pushed)
- `.env` - Private secrets (see `.env.example`)
- `node_modules/` - Too large
- `__pycache__/` - Python cache
- `venv/` - Virtual environment
- `.DS_Store`, `Thumbs.db` - OS files

See `.gitignore` for complete list.

---

## 🔐 Important Security Notes

1. **Never push `.env`** - Contains private keys!
   - Use `.env.example` as template
   - Create `.env` locally with your values

2. **Secrets Management**
   - Store secrets in GitHub Secrets (for CI/CD)
   - Use environment variables in production
   - Rotate keys regularly

3. **For Vercel Deployment**
   - Set environment variables in Vercel dashboard
   - Don't commit `.vercel/` folder
   - Use Vercel's secret management

---

## 📊 Git Workflow

### After Initial Push

**Make Changes:**
```bash
# Edit files
git add .
git commit -m "feat: add new feature"
git push origin main
```

**Create Feature Branch:**
```bash
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "feat: new feature"
git push origin feature/new-feature
# Create Pull Request on GitHub
```

### Useful Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# See changes
git diff

# Undo changes
git checkout -- file.txt

# Delete local branch
git branch -d feature-name

# Delete remote branch
git push origin --delete feature-name
```

---

## 🤝 Collaboration

**Add Collaborators:**
1. Go to Settings → Collaborators
2. Add team members by GitHub username

**Team Workflow:**
1. Main branch = production ready
2. Create feature branches for new work
3. Create Pull Requests for review
4. Merge after approval

---

## 📚 Resources

- [GitHub Guides](https://guides.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

**Ready to push? Run the setup script above! 🚀**
