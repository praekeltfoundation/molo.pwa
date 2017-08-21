import json
from django.views.generic import View
from django.http import HttpResponse


class RegistrationTokenView(View):
    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            data = json.loads(request.body)
            profile = request.user.profile
            profile.registration_token = data['registration_id']
            profile.save()
            return HttpResponse('Token Updated')
        return HttpResponse('User has no profile')
