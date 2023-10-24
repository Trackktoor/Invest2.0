from django.shortcuts import render, HttpResponse
from .models import Item
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