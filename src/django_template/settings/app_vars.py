import os

from .base import BASE_DIR

# django vars
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
APPEND_SLASH = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

EMPLOYEE = "Employee"
MANAGER = "Manager"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT, exist_ok=True)

# env
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))

# REDIS_HOST = os.environ.get('REDIS_HOST')
# RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
#
# # request setup
# REQUEST_TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', 8))
#
# # aws keys
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
# AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION')
#
# DEFAULT_FILE_STORAGE = "django_template.settings.storage_backends.FlexCoreStorage"
#
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
#
# MAX_OTP_ATTEMPTS = 3
# OTP_DIGIT = 6
#
# # SMS CONFIG
# SSL_SMS_GATEWAY_ENDPOINT = os.environ.get('SSL_SMS_GATEWAY_ENDPOINT')
# SMS_SID = os.environ.get('SMS_SID')
# SMS_USER = os.environ.get('SMS_USER')
# SMS_PASSWD = os.environ.get('SMS_PASSD')
# SMS_CSMSID = os.environ.get('SMS_CSMSID')
# SMS_MSISDN = os.environ.get('SMS_MSISDN')