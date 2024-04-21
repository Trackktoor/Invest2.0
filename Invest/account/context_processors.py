from account.models import Profile

def user_context(request):
    return {'user': request.user}

def profile_context(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        print(profile.avatar)
        profile.user.username = profile.user.username.split('_')[0]
        return {'profile':profile}
    return {}
