"""
Django settings for myblogproject - Production Ready (Render.com / Railway / PythonAnywhere)
"""

from pathlib import Path
import os
import dj_database_url  # ← Will be installed via requirements.txt

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key safe in production!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-o(d4xp90py3e7no$d)u+dl#&@k(8_%cvw4y-2ku3td_nh0no2h'  # fallback for local
)

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allow Render and your custom domain
ALLOWED_HOSTS = [
    '*',  # Render gives *.onrender.com
    'localhost',
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'myblogproject',
    'myblogapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # WhiteNoise for static files (MUST be right after SecurityMiddleware)
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblogproject.wsgi.application'

# Database - Works with SQLite locally AND PostgreSQL on Render (if you want later)
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS, Images) - CRITICAL FOR BOOTSTRAP
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']           # Your local static folder
STATIC_ROOT = BASE_DIR / 'staticfiles'             # Where collectstatic puts files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (for future image uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional: Security improvements for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

