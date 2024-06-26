"""
Django settings for ota_server project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mq=17a9pks+1m#um_et98og#oe&0p#+fg@7%)ih$r2zug$pl^k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ota_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ota_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 设置文件上传的最大内存大小为100MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB

# 设置数据上传的最大内存大小为100MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB


OTA_URL = '/ota/'
# OTA_ROOT = os.path.join(BASE_DIR, 'ota')
# 设置上传文件存放的路径
# UPLOAD_BASE_DIR = os.path.join(BASE_DIR, 'uploads/')
# LOG_CONFIG_PATH = os.path.join(UPLOAD_BASE_DIR, 'config/')

# UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads/')
# LOG_CONFIG_FILE_PATH = os.path.join(UPLOAD_DIR, 'config/', 'device_log_config')
# OTA_ROOT = os.path.join(BASE_DIR, 'ota')
# VERSION_INFO_CONFIG_FILE_PATH = os.path.join(OTA_ROOT, 'version_info')
# SERVER_LOG_PATH = os.path.join(OTA_ROOT, 'server.log')

CONFIG_BASE = '/data/config/'
UPLOAD_DIR = '/data/log/'
LOG_CONFIG_FILE_PATH = os.path.join(CONFIG_BASE, 'device_log_config')
OTA_ROOT = '/data/ota/'
VERSION_INFO_CONFIG_FILE_PATH = os.path.join(CONFIG_BASE, 'version_info')
SERVER_LOG_PATH = os.path.join(UPLOAD_DIR, 'server.log')
