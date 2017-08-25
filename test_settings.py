from .base import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'fcm_django',
]

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "eXaMpLeKeY",
    # true if you want to have only one active
    # device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}
