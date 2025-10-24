# Lab 2 Deployment Checklist

Use this checklist to ensure you complete all steps successfully.

---

## Phase 1: Understanding the Changes ✓

- [x] Code has been refactored for external database
- [x] Vercel configuration files created
- [x] Documentation written
- [ ] **YOU: Read `MIGRATION_SUMMARY.md`** ← Start here!
- [ ] **YOU: Read `lab2_writeup.md`** for details
- [ ] **YOU: Read `DEPLOYMENT.md`** for step-by-step guide

---

## Phase 2: Database Setup (Supabase)

### Create Supabase Account
- [ ] Go to https://supabase.com
- [ ] Sign up with GitHub/Gmail/Email
- [ ] Verify email if required

### Create PostgreSQL Database
- [ ] Click "New Project"
- [ ] Enter project name (e.g., "note-taking-app")
- [ ] Set strong database password
- [ ] **SAVE PASSWORD SOMEWHERE SAFE!**
- [ ] Choose region (closest to you)
- [ ] Wait for database to be provisioned (1-2 minutes)

### Get Connection String
- [ ] Go to Project Settings (gear icon)
- [ ] Click "Database" in sidebar
- [ ] Find "Connection string" section
- [ ] Select "URI" format
- [ ] Copy the connection string
- [ ] Replace `[YOUR-PASSWORD]` with your actual password
- [ ] **SAVE CONNECTION STRING!** Format:
  ```
  postgresql://postgres:YOUR_PASSWORD@db.xxx.supabase.co:5432/postgres
  ```

### Screenshot for Writeup
- [ ] Take screenshot of Supabase dashboard
- [ ] Take screenshot of database settings page
- [ ] Save for inclusion in lab2_writeup.md

---

## Phase 3: Local Testing (Optional but Recommended)

### Test with SQLite (Original Behavior)
- [ ] Run `python src/main.py`
- [ ] Visit http://localhost:5001
- [ ] Create a note
- [ ] Verify it works
- [ ] **Screenshot: Working app with SQLite**

### Test with PostgreSQL Locally
- [ ] Create `.env` file in project root
- [ ] Add to `.env`:
  ```
  DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxx.supabase.co:5432/postgres
  SECRET_KEY=any-random-string-here
  FLASK_ENV=development
  ```
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Run: `python src/main.py`
- [ ] Visit http://localhost:5001
- [ ] Create a note
- [ ] Check Supabase dashboard - note should appear in database
- [ ] **Screenshot: Supabase table showing data**

---

## Phase 4: Git Repository Setup

### Commit Changes
- [ ] Run: `git status` (check what changed)
- [ ] Run: `git add .`
- [ ] Run: `git commit -m "Refactor for Vercel deployment with PostgreSQL"`
- [ ] Verify `.env` is NOT committed (check .gitignore)

### Push to GitHub/GitLab
- [ ] Create repository on GitHub if needed
- [ ] Run: `git push origin main` (or master)
- [ ] Verify files are on GitHub
- [ ] **Screenshot: GitHub repository**

---

## Phase 5: Vercel Deployment

### Create Vercel Account
- [ ] Go to https://vercel.com
- [ ] Sign up with GitHub (recommended)
- [ ] Authorize Vercel to access repositories

### Import Project
- [ ] Click "Add New..." → "Project"
- [ ] Find your repository
- [ ] Click "Import"
- [ ] **Screenshot: Import screen**

### Configure Build Settings
- [ ] Framework Preset: **Other** (or leave auto-detected)
- [ ] Root Directory: `./` (default)
- [ ] Build Command: (leave empty)
- [ ] Output Directory: (leave empty)
- [ ] Install Command: `pip install -r requirements.txt` (auto-detected)

### Add Environment Variables ⚠️ IMPORTANT
- [ ] Click "Environment Variables"
- [ ] Add `DATABASE_URL`:
  - Name: `DATABASE_URL`
  - Value: `postgresql://postgres:YOUR_PASSWORD@db.xxx.supabase.co:5432/postgres`
  - Environments: ✓ Production ✓ Preview ✓ Development
- [ ] Add `SECRET_KEY`:
  - Name: `SECRET_KEY`
  - Value: `your-random-secret-key-here`
  - Environments: ✓ Production ✓ Preview ✓ Development
- [ ] Add `FLASK_ENV`:
  - Name: `FLASK_ENV`
  - Value: `production`
  - Environments: ✓ Production ✓ Preview ✓ Development
- [ ] **Screenshot: Environment variables page**

### Deploy
- [ ] Click "Deploy"
- [ ] Wait for build to complete (1-3 minutes)
- [ ] Check for errors in build logs
- [ ] If successful, Vercel provides URL
- [ ] **Screenshot: Successful deployment**

---

## Phase 6: Testing Deployed App

### Basic Functionality
- [ ] Visit your Vercel URL (e.g., https://your-app.vercel.app)
- [ ] **Screenshot: Deployed app homepage**
- [ ] Frontend loads correctly
- [ ] No console errors (open browser DevTools)

### CRUD Operations
- [ ] Click "New Note" button
- [ ] Enter title: "Test Note 1"
- [ ] Enter content: "This is a test note on Vercel"
- [ ] Click "Save"
- [ ] **Screenshot: Created note**
- [ ] Refresh page
- [ ] Note still exists (data persisted)
- [ ] Click the note to edit
- [ ] Change content
- [ ] Click "Save"
- [ ] **Screenshot: Updated note**
- [ ] Create another note: "Test Note 2"
- [ ] Search for "test" in search box
- [ ] Both notes appear
- [ ] **Screenshot: Search results**
- [ ] Click delete on one note
- [ ] Confirm deletion
- [ ] Note disappears
- [ ] **Screenshot: After deletion**

### Database Verification
- [ ] Go to Supabase dashboard
- [ ] Check "Table Editor"
- [ ] See `note` table with your data
- [ ] **Screenshot: Supabase table with data**

---

## Phase 7: Documentation

### Update lab2_writeup.md
- [ ] Add screenshots to appropriate sections
- [ ] Fill in "Testing Process" section with your results
- [ ] Add any challenges you encountered
- [ ] Add your observations to "Lessons Learned"
- [ ] Include your Vercel deployment URL
- [ ] Include your Supabase project URL

### Screenshot Checklist
Required screenshots:
- [ ] Supabase dashboard showing project
- [ ] Supabase database connection settings
- [ ] Supabase table editor showing data
- [ ] GitHub repository with code
- [ ] Vercel import/configuration screen
- [ ] Vercel environment variables
- [ ] Vercel deployment success
- [ ] Deployed app homepage
- [ ] Creating a note
- [ ] Editing a note
- [ ] Search functionality
- [ ] Deleted note confirmation

---

## Phase 8: Final Verification

### Code Review
- [ ] All files committed to Git
- [ ] `.env` file NOT committed (in .gitignore)
- [ ] No hardcoded secrets in code
- [ ] `requirements.txt` has all dependencies

### Documentation Review
- [ ] `lab2_writeup.md` is complete
- [ ] All screenshots embedded/attached
- [ ] Challenges and solutions documented
- [ ] Lessons learned section filled out

### Deployment Check
- [ ] Vercel URL works
- [ ] Database connected
- [ ] All features working
- [ ] Data persists

---

## Phase 9: Submission Preparation

### Files to Submit
- [ ] `lab2_writeup.md` (main deliverable)
- [ ] Screenshots (embedded in writeup or separate folder)
- [ ] Vercel deployment URL
- [ ] GitHub repository URL (if required)

### Information to Include
- [ ] Student name/ID
- [ ] Vercel deployment URL: `https://_____.vercel.app`
- [ ] GitHub repository: `https://github.com/_____`
- [ ] Supabase project name: `_____`
- [ ] Any special instructions

---

## Troubleshooting

### If Build Fails on Vercel
1. Check build logs in Vercel dashboard
2. Common issues:
   - Missing dependencies in `requirements.txt`
   - Python version mismatch
   - Import errors
3. Fix locally, commit, push → auto-redeploys

### If Database Connection Fails
1. Check environment variables in Vercel
2. Verify DATABASE_URL format
3. Test connection from local machine
4. Check Supabase database is active
5. Ensure password is correct in connection string

### If Frontend Doesn't Load
1. Check Vercel function logs
2. Verify `vercel.json` routes
3. Check browser console for errors
4. Ensure static files in `src/static/`

### If Data Doesn't Persist
1. Check Vercel logs for database errors
2. Verify environment variables set correctly
3. Check Supabase database is accessible
4. Test queries in Supabase SQL editor

---

## Resources

- **Quick Start**: `MIGRATION_SUMMARY.md`
- **Detailed Steps**: `DEPLOYMENT.md`
- **Full Documentation**: `lab2_writeup.md`
- **Environment Template**: `.env.example`

---

## Success Criteria

You're done when:
- ✅ App deployed to Vercel
- ✅ Using PostgreSQL database (not SQLite)
- ✅ All CRUD operations work
- ✅ Data persists across requests
- ✅ Environment variables configured
- ✅ Documentation complete with screenshots
- ✅ No secrets committed to Git

---

## Estimated Time

- Phase 1 (Reading): 15 minutes
- Phase 2 (Database): 10 minutes
- Phase 3 (Local Testing): 15 minutes
- Phase 4 (Git): 5 minutes
- Phase 5 (Vercel): 15 minutes
- Phase 6 (Testing): 20 minutes
- Phase 7 (Documentation): 30 minutes
- **Total: ~2 hours**

---

## Need Help?

1. Check `DEPLOYMENT.md` troubleshooting section
2. Check Vercel function logs
3. Check Supabase database logs
4. Review `lab2_writeup.md` for detailed explanations

---

**Good luck! 🚀**

Start with Phase 1 and work through each phase systematically.
