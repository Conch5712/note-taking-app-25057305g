# Deployment Guide for Vercel

This guide explains how to deploy the note-taking application to Vercel with an external PostgreSQL database.

## Prerequisites

1. A Vercel account (sign up at https://vercel.com)
2. A PostgreSQL database (we recommend Supabase: https://supabase.com)
3. Git repository (GitHub, GitLab, or Bitbucket)

## Step 1: Set Up PostgreSQL Database

### Option A: Using Supabase (Recommended)

1. Go to https://supabase.com and sign up/login
2. Create a new project
3. Wait for the database to be provisioned
4. Go to Project Settings > Database
5. Copy the "Connection string" (URI format)
   - It will look like: `postgresql://postgres:[YOUR-PASSWORD]@db.xxx.supabase.co:5432/postgres`

### Option B: Using Other Providers

You can also use:
- Railway (https://railway.app)
- Neon (https://neon.tech)
- Heroku Postgres
- AWS RDS
- Any PostgreSQL provider

Just make sure you have the connection string in this format:
```
postgresql://username:password@host:port/database
```

## Step 2: Prepare Your Repository

1. Make sure all changes are committed to Git
2. Push your code to GitHub, GitLab, or Bitbucket

```bash
git add .
git commit -m "Prepare for Vercel deployment with PostgreSQL"
git push origin main
```

## Step 3: Deploy to Vercel

1. Go to https://vercel.com/dashboard
2. Click "Add New..." > "Project"
3. Import your Git repository
4. Configure your project:
   - Framework Preset: **Other**
   - Root Directory: `./` (leave as default)
   - Build Command: (leave empty)
   - Output Directory: (leave empty)

## Step 4: Configure Environment Variables

In the Vercel project settings, add the following environment variables:

### Required Variables:

1. **DATABASE_URL**
   - Value: Your PostgreSQL connection string from Step 1
   - Example: `postgresql://postgres:password@db.xxx.supabase.co:5432/postgres`

2. **SECRET_KEY**
   - Value: A secure random string (generate one)
   - Example: `your-super-secret-key-here-change-this`

3. **FLASK_ENV**
   - Value: `production`

### Optional Variables (for future LLM features):

- **OPENAI_API_KEY** (if using OpenAI)
- **ANTHROPIC_API_KEY** (if using Claude)

### How to Add Environment Variables in Vercel:

1. In your Vercel project dashboard
2. Go to Settings > Environment Variables
3. Add each variable:
   - Name: `DATABASE_URL`
   - Value: `postgresql://...`
   - Environment: Production, Preview, Development (check all)
4. Click "Save"

## Step 5: Deploy

1. Click "Deploy" button
2. Wait for the build to complete (usually 1-2 minutes)
3. Once deployed, Vercel will provide you with a URL (e.g., `https://your-app.vercel.app`)

## Step 6: Verify Deployment

1. Visit your deployment URL
2. Try creating, editing, and deleting notes
3. Check that data persists across page refreshes

## Troubleshooting

### Issue: "Module not found" errors

- Make sure all dependencies are listed in `requirements.txt`
- Redeploy after updating requirements

### Issue: Database connection errors

- Verify your DATABASE_URL is correct
- Check that your PostgreSQL database is accessible from external connections
- For Supabase, ensure the connection pooler port (6543) is NOT used - use the direct port (5432)

### Issue: 500 Internal Server Error

- Check the Vercel function logs in the dashboard
- Go to Deployments > Your Deployment > Functions tab
- Look for error messages

### Issue: Static files not loading

- Ensure the `src/static` directory exists
- Check that `vercel.json` routes are configured correctly

## Local Testing with PostgreSQL

To test locally with PostgreSQL before deploying:

1. Create a `.env` file in the root directory:
```
DATABASE_URL=postgresql://your-connection-string
SECRET_KEY=your-secret-key
FLASK_ENV=development
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py
```

4. Visit http://localhost:5001

## Updating Your Deployment

Vercel automatically redeploys when you push to your Git repository:

```bash
git add .
git commit -m "Update feature"
git push origin main
```

Vercel will automatically detect the push and redeploy your application.

## Important Notes

- **Database Persistence**: Data is now stored in PostgreSQL, which persists across deployments
- **Serverless Functions**: Each request runs in a separate serverless function
- **Cold Starts**: First request after inactivity may be slower (cold start)
- **Connection Pooling**: Consider using connection pooling for better performance in production
- **Backups**: Make sure to back up your PostgreSQL database regularly

## Support

For issues:
- Vercel Documentation: https://vercel.com/docs
- Supabase Documentation: https://supabase.com/docs
- Flask Documentation: https://flask.palletsprojects.com/
