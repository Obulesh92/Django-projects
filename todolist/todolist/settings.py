import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ←←← CHANGE THESE 4 LINES ONLY ←←←
DEBUG = False                                   # was True
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key-for-render")
ALLOWED_HOSTS = ["*"]                           # Render needs this for free *.onrender.com domains

# Add WhiteNoise (just these 3 lines)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ← add this line
    # ... keep all your existing middleware below
]

# Static files – keep your existing lines + add these 2
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")          # ← change from 'assets'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# CSRF (add this block at the bottom)
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]
