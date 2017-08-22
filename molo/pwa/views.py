import json
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

from . import app_settings


class RegistrationTokenView(View):
    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            data = json.loads(request.body)
            profile = request.user.profile
            profile.registration_token = data['registration_id']
            profile.save()
            return HttpResponse('Token Updated')
        return HttpResponse('User has no profile')


def service_worker(request):
    response = HttpResponse(open(app_settings.PWA_SERVICE_WORKER_PATH).read(),
                            content_type='application/javascript')
    return response


def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    })
