# QuizCraft

QuizCraft is an advanced AI-powered quiz generation platform that leverages Google's Gemini AI to create, customize, and share interactive quizzes. The application supports multiple question types and can generate quizzes from various file formats including PDF, DOCX, TXT, CSV, and images.

## Features

- **AI-Powered Quiz Generation**: Create quizzes from text input or uploaded files using Google Gemini 1.5 Pro
- **Multiple File Type Support**: Process PDF, DOCX, TXT, CSV, and image files (JPG, PNG) for quiz generation
- **Multiple Question Types**: Support for multiple-choice, true/false, fill-in-the-blank, and short answer questions
- **User Authentication**: Complete user management with registration, login, and profile management
- **Quiz Management**: Create, edit, share, and delete quizzes
- **Quiz Taking**: Take quizzes with automatic scoring and result tracking
- **PDF Export**: Export quizzes and results as PDF documents
- **Responsive Design**: Modern, responsive UI using Tailwind CSS

## Tech Stack

- **Backend**: Flask web framework (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **AI**: Google Gemini 1.5 Pro API
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **File Processing**: PyPDF2, python-docx, pdf2image, pytesseract (OCR)

## Prerequisites

- Python 3.10+
- PostgreSQL
- Tesseract OCR (optional, for image processing)
- Google Gemini API key

## Setup for VS Code Development

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/quizcraft.git
cd quizcraft
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r project_requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with the following variables:

```
# Flask configuration
FLASK_APP=main.py
FLASK_ENV=development
SESSION_SECRET=your-secret-key

# Database connection
DATABASE_URL=postgresql://username:password@localhost:5432/quizcraft

# Google Gemini API key
GEMINI_API_KEY=your-gemini-api-key

# Application settings
DEBUG=True
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=52428800  # 50MB in bytes
```

### 5. Set up the database

Create a PostgreSQL database and update the `DATABASE_URL` in your `.env` file.

### 6. Create required directories

```bash
mkdir -p uploads instance
```

### 7. Run the application

```bash
flask run
```

The application will be available at `http://localhost:5000`.

## VS Code Configuration

### Recommended Extensions

- Python (Microsoft)
- Pylance
- SQLite Viewer
- markdownlint
- Git Lens
- Docker (if using containerization)
- Python Test Explorer
- HTML/CSS/JavaScript support

### Settings.json

Create a `.vscode/settings.json` file with the following configuration:

```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "100"],
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true
  },
  "python.testing.pytestEnabled": true,
  "python.terminal.activateEnvironment": true
}
```

### Launch.json

Create a `.vscode/launch.json` file for debugging:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "main.py",
        "FLASK_ENV": "development",
        "FLASK_DEBUG": "1"
      },
      "args": ["run", "--no-debugger", "--host=0.0.0.0"],
      "jinja": true
    }
  ]
}
```

## Project Structure

```
quizcraft/
├── app.py               # App initialization and configuration
├── config.py            # Configuration classes
├── forms.py             # Form definitions
├── main.py              # Application entry point
├── migrations.py        # Database migrations
├── instance/            # Instance-specific data (SQLite DB if used)
├── models/              # Database models
│   ├── __init__.py
│   ├── quiz.py          # Quiz-related models
│   └── user.py          # User model
├── routes/              # Route definitions
│   ├── __init__.py
│   ├── api.py           # API endpoints
│   ├── auth.py          # Authentication routes
│   └── quiz.py          # Quiz-related routes
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # Jinja2 templates
│   ├── auth/
│   ├── base.html
│   ├── errors/
│   └── quiz/
├── uploads/             # User file uploads
└── utils/               # Utility functions
    ├── __init__.py
    ├── ocr_handler.py   # OCR text extraction
    └── quiz_generator.py # AI quiz generation
```

## License

[MIT License](LICENSE)