import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
# This needs to be done before importing app
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

from app import app
from routes import register_routes

# Register routes
register_routes(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "True").lower() in ("true", "1", "t")
    app.run(host="0.0.0.0", port=port, debug=debug)
