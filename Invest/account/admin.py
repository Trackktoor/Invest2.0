from django.contrib import admin  # pylint: disable=all
from .models import Profile, ProfileImage
# Register your models here.

admin.site.register(Profile)
admin.site.register(ProfileImage)

