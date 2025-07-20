import os  
from pathlib import Path  


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-6=w3+g1o@=@rk$uxak18sr%ic#cqr^ld3a*)0+@zbv2!rrn167')  



DEBUG = os.getenv('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'hilario2.pythonanywhere.com'] 


CSRF_TRUSTED_ORIGINS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",  
    'project_twitter.twitter.apps.TwitterConfig',  
    "rest_framework", 
    "rest_framework.authtoken",  
    "django.contrib.humanize", 
    'widget_tweaks',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
]


ROOT_URLCONF = "project_twitter.urls"

# Configuração de templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "twitter", "templates")], 
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "project_twitter.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),  
        "NAME": str(os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3")), 
        "USER": os.environ.get("SQL_USER", "user"),  
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),  
        "HOST": os.environ.get("SQL_HOST", "localhost"),  
        "PORT": os.environ.get("SQL_PORT", "5432"),  
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "pt-br"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


if DEBUG:
    STATICFILES_DIRS = [
        
    ]


LOGIN_REDIRECT_URL = '/twitter/'  
LOGOUT_REDIRECT_URL = '/login/'  
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# if DEBUG:
#    INTERNAL_IPS = [
#        "127.0.0.1",
#    ]
