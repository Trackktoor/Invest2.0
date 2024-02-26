from django.contrib.auth.models import User
from django.shortcuts import render,redirect,resolve_url
from .forms import SignupForm
from .models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str 
from .token import account_activation_token
from django.core.mail import EmailMessage 
from account.models import Profile
from django.contrib.auth import login
from account.models import ProfileImage
from django.http import JsonResponse
from .forms import SignupForm
from django.core.files.base import File
from django.contrib.auth.decorators import login_required
from PIL import Image
import hashlib
from Invest.settings import BASE_DIR
from invest_projects.models import Item


def calculate_image_hash(image):
    with Image.open(image) as img:
        img_hash = hashlib.md5(img.tobytes()).hexdigest()
    return img_hash


def Signup(request):
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
            cleaned_data = form.cleaned_data
            return render(request, 'account/signup.html', {'form':form, "cleaned_data": cleaned_data, 'errors':form.errors})


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
    print(profile)
    return render(request, 'account/profile.html', {'current_profile':profile})

@login_required
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'account/edit_profile.html')
    
    if request.method == 'POST':
        print(request.POST)
        profile_bd = Profile.objects.get(user=request.user)
        if 'avatar' not in request.FILES.keys():
            request.FILES['avatar'] = False 
        avatar = request.FILES['avatar'] or profile_bd.avatar
        if request.POST['username']:
            username = request.POST['username']
        else:
            username = profile_bd.user.username

        status = request.POST['status'] or profile_bd.profile_status
        profile_info = request.POST['profile_info'].strip() or profile_bd.profile_info

        # for profile_image in profile_bd.images.all():
        #     for img_path in images_in_post:
        #         img_path_post = img_path.replace('/', '\\')
        #         img_path_bd = profile_image.image.path

        #         if img_path_post in img_path_bd.replace('/', '\\'):
        #             images_in_post.remove()
        #             continue
        #         else:
        #             print(f"{img_path} not in {profile_image.image.path}")
        #             profile_bd.images.remove(profile_image)
        #             profile_image.delete()

        # print(profile_bd.images.all())
        # profile_bd.save()
        # print(images_in_post)
        # for photo_url in images_in_post:
        #     full_path = os.path.join(BASE_DIR, photo_url[1:])
        #     photos_content.append(full_path)
        #     print('APPEND_POST')
        if len(request.FILES.getlist('images')) == 0:
            for img in profile_bd.images.all():
                img.delete()
        else:
            for image in profile_bd.images.all():
                image.delete()
                
            photos_content = []

            for photo_file in request.FILES.getlist('images'):
                    print('APPEND_FILES')
                    photos_content.append(photo_file)
            for image in photos_content:
                img_bd = ProfileImage.objects.create(profile=profile_bd.id, image=image)
                profile_bd.images.add(img_bd)
                print('!!!!')

        profile_bd.avatar = avatar
        profile_bd.user.username = username
        profile_bd.profile_status = status
        profile_bd.profile_info = profile_info

        profile_bd.save()
        profile_bd.user.save()

        data = {
            'status': 200,
            'reverse_url': resolve_url(profile, user_id=request.user.id)
        }

        return JsonResponse(data)

@login_required
def my_projects(request):
    if request.method == 'GET':
        projects = Item.objects.filter(user=request.user)
        return render(request, 'account/my_projects.html', {'projects':projects})