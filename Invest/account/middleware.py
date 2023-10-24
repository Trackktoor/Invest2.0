from datetime import datetime
from django.contrib.auth.models import User
from .models import Profile
import pytz


class LastActivityUpdateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            profile.last_acivity = datetime.now().replace(tzinfo=pytz.UTC)
            profile.save()

        return response
