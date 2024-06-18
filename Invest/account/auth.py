"""
    Файд для кастомной авторизации
"""

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = User.objects.get(**kwargs)
            print(user)
            if user.check_password(password):
                print('e')
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
