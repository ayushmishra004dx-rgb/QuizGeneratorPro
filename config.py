import os

class Config:
    """Base configuration class for QuizCraft application."""
    # Flask settings
    SECRET_KEY = os.environ.get("SESSION_SECRET", "quizcraft-dev-secret")
    DEBUG = True
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///quizcraft.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Google Gemini API settings
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
    
    # File upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size (increased from 16MB)
    UPLOAD_FOLDER = "uploads"
    ALLOWED_EXTENSIONS = {
        'txt', 'pdf', 'doc', 'docx', 'csv',  # Documents
        'png', 'jpg', 'jpeg'  # Images for OCR
    }
    
    # Quiz generation settings
    DEFAULT_NUM_QUESTIONS = 10
    MIN_QUESTIONS = 5
    MAX_QUESTIONS = 75
    
    # Brand colors
    PRIMARY_COLOR = "#3B82F6"  # Blue
    ACCENT_COLOR = "#10B981"   # Green
    ERROR_COLOR = "#EF4444"    # Red
