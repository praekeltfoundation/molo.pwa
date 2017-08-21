from django.conf.urls import patterns, url

from fcm_django.api.rest_framework import FCMDeviceViewSet
from rest_framework.routers import DefaultRouter

from .views import RegistrationTokenView


urlpatterns = patterns('', )

router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)

urlpatterns += patterns(
    '',
    url(
        r'^notification_devices/$', RegistrationTokenView.as_view(),
        name='registration-token'),
)
