

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i)#(liiohgcu5y7o*6@gkqcm_%zz+pdcljil%pt)uu^b-v2v)s'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'histerdans14@gmail.com'
EMAIL_HOST_PASSWORD = '**************'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Jiuze MarketPlace <histerdans14@gmail.com>'
BASE_URL = '127.0.0.1:8000, localhost:8000'


MANAGERS = (
    ('Daniel', "histerdans14@gmail.com"),
)

ADMINS = MANAGERS



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party

    #our apps
    'accounts',
    'addresses',
    'analytics',
    'billing',
    'carts',
    'marketing',
    'orders',
    'products',
    'search',
    'tags',
]

AUTH_USER_MODEL = 'accounts.User' #changes the built-in user model to ours
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION= False



MAILCHIMP_API_KEY = ""
MAILCHIMP_DATA_CENTER = "us17"
MAILCHIMP_EMAIL_LIST_ID = ""

if DEBUG:

    STRIPE_SECRET_KEY = ""
    STRIPE_PUB_KEY = ''

else:

    STRIPE_SECRET_KEY = "sk_test_cu1lQmcg1OLffhLvYrSCp5XE"
    STRIPE_PUB_KEY = 'pk_test_PrV61avxnHaWIYZEeiYTTVMZ'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'JiuzeSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'JiuzeSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'jiuzedata.db'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")


PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "protected_media")



from JiuzeSite.aws.conf import *


CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False



