import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'r0k9of*6n#5ux92%)p2d8eevdg_tir)0d7@6!cyf2dwck-ng4p'

DEBUG = True
ALLOWED_HOSTS = ['*']

##########################################
#####             APPS              ######
##########################################

INSTALLED_APPS = [
    # Estilização do admin
    'core.SuitConfig',
    # Módulos base
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Bibliotecas adicionais
    'rest_framework',
    'crispy_forms',

    # Módulos clinica
    'core',
    'usuarios',
    'paciente',
    'empresa',
    'auxiliar',
    'agenda',
    'receituario',
    'laboratorial',
    'oftalmologia',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
ROOT_URLCONF = 'core.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.tenant.TenantMiddleware'
]

##########################################
#####           TEMPLATES           ######
##########################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "core", 'templates'),
            os.path.join(BASE_DIR, "receituario", 'templates'),
            os.path.join(BASE_DIR, "axuiliar", 'templates'),
            os.path.join(BASE_DIR, "empresa", 'templates'),
            os.path.join(BASE_DIR, "paciente", 'templates'),
            os.path.join(BASE_DIR, "usuarios", 'templates'),
            os.path.join(BASE_DIR, "laboratorial", 'templates'),
            os.path.join(BASE_DIR, "agenda", 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

##########################################
#####           DATABASE             ######
##########################################

MYSQL = False

if MYSQL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'clinica',
            'PORT': 3308,
            'USER': 'root',
            'HOST': '127.0.0.1',
            'PASSWORD': 'secret',
            'ATOMIC_REQUESTS': True,
            'OPTIONS': {
                'charset': 'utf8mb4',
                'use_unicode': True, },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

##########################################
##### VALIDADORES                   ######
##########################################

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

##########################################
##### CONFIGURAÇÕES DE AUTENTICAÇÃO ######
##########################################

ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

##########################################
#####                    EMAIL SMTP ######
##########################################

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '1c21935a501512'
EMAIL_HOST_PASSWORD = 'aedaf929f903aa'
EMAIL_PORT = '2525'

##########################################
##### CONFIGURAÇÕES DE AUTENTICAÇÃO ######
##########################################

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
DATE_FORMAT = "d/m/Y"
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y')
USE_L10N = False
USE_TZ = False

##########################################
##### USER MODEL                    ######
##########################################

AUTH_USER_MODEL = 'core.User'

##########################################
##### ESTÁTICOS                     ######
##########################################

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

##########################################
##### CACHE                         ######
##########################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache-clinica',
    }
}
