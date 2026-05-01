import os

# Set API_URL using environment variables for deployment, fallback to the hardcoded Render URL
API_URL = os.getenv("API_URL", "https://medicalassistant-wl4w.onrender.com")