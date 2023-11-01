from django.shortcuts import render, HttpResponse
from .models import Item, Category, ItemImage
from account.models import Profile
from django.contrib.auth.decorators import login_required
from account.models import Profile

# Create your views here.

def AllInvestProjects(request):
    if request.method == 'GET':
        return render(request, 'invest_projects/AllInvestProjects.html')
    
def Project(request,project_id):
    if request.method == 'GET':
        try:
            project = Item.objects.get(id=project_id)
            profile = Profile.objects.get(user=project.user)
            return render(request, 'invest_projects/InvestProject.html', {'project':project,'profile':profile})

        except Item.DoesNotExist: 
            return HttpResponse('<h1 styles="text-align=center">404 Not Found</h1>')

@login_required
def AddProject(request):
    if request.method == 'GET':
        profile = Profile.objects.get(user=request.user)
        return render(request, 'invest_projects/AddProject.html', {'profile':profile})
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        city = request.POST['city']
        required_investment = request.POST['required_investment']
        profit_per_month = request.POST['profit_per_month']
        profit_parameter = request.POST['profit_parametr']
        category = Category.objects.first()
        #Создать здесь картинки
        background_image = request.FILES['background_image']
        project_avatar = request.FILES['project_avatar']
        contacts = request.POST['contacts']
        author_job_title = request.POST['author_job_title']

        # project = Item(
        #     title=title,
        #     description=description,
        #     city=city,
        #     required_investment=required_investment,
        #     profit_per_month=profit_per_month,
        #     profit_parametr=profit_parameter,
        #     author_job_title=author_job_title,
        #     contacts=contacts,
        #     user=request.user
        # )

        # Проверить, существует ли проект с таким заголовком и автором
        existing_project = Item.objects.filter(title=title, user=request.user).first()

        if existing_project:
            # Если проект существует, обновить его данные
            existing_project.description = description
            existing_project.city = city
            existing_project.required_investment = required_investment
            existing_project.profit_per_month = profit_per_month
            existing_project.profit_parameter = profit_parameter
            existing_project.author_job_title = author_job_title
            existing_project.contacts = contacts
            existing_project.background_image = background_image
            existing_project.project_avatar = project_avatar
            existing_project.category.set([Category.objects.first()])

            # Сохранить обновленный проект
            existing_project.save()

            # Очистить существующие изображения и добавить новые
            existing_project.images.clear()
            for photo in request.FILES.getlist('images'):
                new_image = ItemImage(item=existing_project, image=photo)
                new_image.save()
        else:
            # Если проект не существует, создать новый
            project = Item(
                title=title,
                description=description,
                city=city,
                required_investment=required_investment,
                profit_per_month=profit_per_month,
                profit_parametr=profit_parameter,
                author_job_title=author_job_title,
                contacts=contacts,
                user=request.user,
                background_image=background_image,
                project_avatar=project_avatar,
            )
            project.save()
            project.category.add(Category.objects.first())


        project.save()
        project.category.add(Category.objects.first())

        for photo in request.FILES.getlist('images'):
            new_image = ItemImage(item=project, image=photo)
            new_image.save()

        print(project)
        return HttpResponse(str(request.POST))

        # for photo in request.FILES.getlist('images'):
        #     print("!!!!!!!!!!!!")
        #     print(project.id)
        #     new_image = ItemImage(item_id=project.id, image=photo)
        #     new_image.save()
        #     project.images.add(new_image)
        # project.category.add(Category.objects.first())
        # project.save()
        #
        # print(project)
        # return HttpResponse(str(request.POST))
