import os

# Set API_URL using environment variables for deployment, fallback to the local backend port
API_URL = os.getenv("API_URL", "http://localhost:8000")