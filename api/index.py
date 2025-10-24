"""
Vercel serverless function entry point
This file is required for Vercel Python serverless functions
"""
import sys
import os

# Add the parent directory to the path to import src modules
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app

# Export the Flask app for Vercel
# Vercel will look for a variable named 'app' or a function named 'handler'
handler = app
