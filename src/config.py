import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration class"""

    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdf#FGSgvasgf$5$WGT'

    # Database configuration
    # Priority: DATABASE_URL > SQLite fallback (for local development)
    DATABASE_URL = os.environ.get('DATABASE_URL')

    if DATABASE_URL:
        # Fix for Heroku/some providers that use 'postgres://' instead of 'postgresql://'
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Fallback to SQLite for local development
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'database', 'app.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask environment
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')

    # Optional: LLM API Keys (for future use)
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

    @staticmethod
    def init_app(app):
        """Initialize application with configuration"""
        pass
