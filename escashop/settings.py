"""
Django settings for oscardemo project.
Generated by 'django-admin startproject' using Django 1.8.8.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from oscar import get_core_apps
from oscar.defaults import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0u!2w1xt06#j39d^7o(@!e&ro2mi^g=3^h-m#b&ld)t03m)15d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'oscar',
    'core',
    'django.contrib.admin',
    'el_pagination',
    'markdown_deux',
    'pagedown',
    'simpleblog',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'escashop.urls'

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            OSCAR_MAIN_TEMPLATE_DIR,
            ],
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

WSGI_APPLICATION = 'escashop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-in'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


#####################################################
# oscardemo modifications for 1.initial-setup       #
#####################################################

# standard django statis and media settings

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# this includes all the oscar default settins
from oscar.defaults import *

from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps

TEMPLATES[0]['DIRS'] = [
    os.path.join(BASE_DIR, 'templates'),
    # this "hack" allows to access the oscar templates using standard path e.g. /home.html
    # but also prefixed with /oscar/ e.g. /oscar/home.html
    # this allows to extend oscar templates, we will see an example of this later
    OSCAR_MAIN_TEMPLATE_DIR
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
]

INSTALLED_APPS += [
    'django.contrib.sites',
    'django.contrib.flatpages',
    # django-compressor is used for compiling static assets
    'compressor',
    # django-widget-tweaks allows some nice customization of html forms rendring from templates
    # it's used in the default oscar temlpates
    'widget_tweaks',
    # django oscar is split into many apps
] + get_core_apps(['oscardemo.promotions'])

SITE_ID = 1

MIDDLEWARE_CLASSES += [
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# haystack is a search engine module for django
HAYSTACK_CONNECTIONS = {
    'default': {
        # django-oscar only supports SimpleEngine which has no special dependencies or SolrEngine
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# django oscar recommends using ATOMIC_REQUESTS
DATABASES['default']['ATOMIC_REQUESTS'] = True

# oscar has status for entire order, or per line
# the status names and pipeline is fully customizable here
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_DEFAULT_CURRENCY = "INR"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

OSCAR_MISSING_IMAGE_URL = MEDIA_URL + 'image_not_found.jpg'

from django.utils.translation import ugettext_lazy as _

OSCAR_DASHBOARD_NAVIGATION += [{
    'label': _('Payments'),
    'icon': 'icon-globe',
    'children': [
        {
            'label': _('Paypal Express transactions'),
            'url_name': 'paypal-express-list',
        },
        {
            'label': _('COD Transaction Lists'),
            'url_name': 'cashondelivery-transaction-list',
        },
    ]
}]

OSCAR_SHOP_NAME = 'Escahub'
OSCAR_SHOP_TAGLINE = "It's a huge world, 'Lets get an Escape with Esca'"

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

PAYPAL_API_USERNAME = 'ripudaman_api1.approapp.com'
PAYPAL_API_PASSWORD = 'QRBUZVUPGUGN2FU7'
PAYPAL_API_SIGNATURE = 'AFGD4eaPO10uIEZq1EDEP1hGh04xAEu3v-T4PBZj-PttRlPTc19zqCpv'

INSTALLED_APPS += ['paypal']
