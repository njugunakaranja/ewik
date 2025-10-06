from pathlib import Path

# --- Base Directory ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security ---
SECRET_KEY = 'django-insecure-&kyh7%a233mr1m$hx4d@i$m#@4t)eedqu_e(q03v1l^*7n&g4o'
DEBUG = True
ALLOWED_HOSTS = []

# --- Installed Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # Your custom app
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URL Configuration ---
ROOT_URLCONF = 'ewik.urls'

# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates folder
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

# --- WSGI ---
WSGI_APPLICATION = 'ewik.wsgi.application'

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# --- Static Files ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

# --- Media Files ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Default Primary Key ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'