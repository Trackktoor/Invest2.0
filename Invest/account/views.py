from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import SignupForm
from .models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str 
from .token import account_activation_token
from django.core.mail import EmailMessage 
from .forms import ItemForm, SupportMailForm
from account.models import Profile
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from .forms import SupportMailForm
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

def Sugnup(request):
    """
        Вьюшка для регистрации через почту
    """
    if request.method == 'GET':
        return render(request,'account/signup.html')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.username = '_'.join([request.POST['name'], str(user.pk)])
            user.save()
            profile = Profile(
                user=user,
                phone_number=request.POST['phone'],
                interest=request.POST['interest']
            )
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Ссылка для активации отправлена ​​на ваш адрес электронной почты'
            message = render_to_string('account/acc_activate_email.html',
                {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                }
            )
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            email.send()
            return render(request, 'account/signup_link_send.html')
        else:
            return render(request, 'account/signup.html', {'form':form, 'errors':form.errors})

    if request.method == 'GET':
        form = SignupForm()
    return render(request, 'account/signup.html')

def LogIn(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        Profile.objects.get(user=user).save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('all_projects')
    else:
        return render(request, 'account/signup_link_error.html')
    
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    return render(request, 'account/profile.html', {'profile':profile})