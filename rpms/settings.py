from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    "tinymce",
    
    'easy_thumbnails'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rpms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "web.context_processors.main_context",
            ],
        },
    },
]

WSGI_APPLICATION = 'rpms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Define DATABASES (postgres-production)
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
        "USER": config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": "5432",
        'OPTIONS': {},
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True


USE_L10N = False
DATE_INPUT_FORMATS = (
    "%d/%m/%Y",
    "%d-%m-%Y",
    "%d/%m/%y",
    "%d %b %Y",
    "%d %b, %Y",
    "%d %b %Y",
    "%d %b, %Y",
    "%d %B, %Y",
    "%d %B %Y",
)
DATETIME_INPUT_FORMATS = (
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M",
    "%d/%m/%Y",
    "%d/%m/%y %H:%M:%S",
    "%d/%m/%y %H:%M",
    "%d/%m/%y",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

THUMBNAIL_ALIASES = {"": {"small": {"size": (960, 430), "crop": True},"extra_small":{"size": (200, 200), "crop": True}, "medium": {"size": (800, 1200), "crop": False},"banner": {"size": (1660, 430), "crop": True}}}
THUMBNAIL_BASEDIR = "thumbnails"


