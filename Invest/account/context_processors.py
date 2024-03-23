from account.models import Profile

def user_context(request):
    return {'user': request.user}

def profile_context(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        print(profile.avatar)
        return {'profile':profile}
    return {}
