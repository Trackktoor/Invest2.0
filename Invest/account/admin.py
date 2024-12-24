from django.contrib import admin  # pylint: disable=all
from .models import Profile, ProfileImage, ProfileVideo
# Register your models here.

admin.site.register(Profile)
admin.site.register(ProfileImage)
admin.site.register(ProfileVideo)

