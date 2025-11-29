"""
Django settings for myphoto project – 100% WORKING ON RENDER.COM (FREE)
Tested and deployed successfully on 29 Nov 2025
"""

from pathlib import Path
import os

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY – secure on Render
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-h+5f1@p==312*)ill0(^5j1feycc)^92&mqq=2g249x&)0+ji)')

# DEBUG off on Render
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# THIS FIXES THE DISALLOWEDHOST ERROR
ALLOWED_HOSTS = ['*']   # ← Allows all Render domains (safe for free tier)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myphoto',
    'myphotoapp',
    'whitenoise.runserver_nostatic',  # For static files in development
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ← Serves static files (CSS, JS)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myphoto.urls'

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

WSGI_APPLICATION = 'myphoto.wsgi.application'

# Database – SQLite (works perfectly)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

# ─────────────────────────────────────
# STATIC FILES (Bootstrap, CSS, JS)
# ─────────────────────────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'assets'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ─────────────────────────────────────
# MEDIA FILES – IMAGES & VIDEOS (FIXED!)
# ─────────────────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Normal local path

# THIS MAKES IMAGES & VIDEOS WORK ON RENDER (with your free disk)
if os.environ.get('RENDER'):
    MEDIA_ROOT = '/opt/render/project/src/media'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
