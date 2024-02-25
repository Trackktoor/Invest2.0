from .models import Item, ItemImage
from django.db.models.fields.files import ImageFieldFile
from django.http import JsonResponse
from django.db.models import F, Value
from django.core import serializers
from django.db.models.functions import Concat
from django.db.models import CharField
from django.core.serializers import serialize

def projects_map(project):
    images_urls = [item_image.image.url for item_image in project.images.all()]
    
    project_dict = project.__dict__
    project_dict = {key: value for key, value in project_dict.items() if not key.startswith('_')}
    for key in project_dict.keys():
        if type(project_dict[key]) == ImageFieldFile:
            project_dict[key] = project_dict[key].url
    project_dict['category'] = project.category.first().title
    project_dict['images_urls'] = images_urls
    return project_dict


def GetAllInvestProjects(request):
    if "HTTP_X_REQUESTED_WITH" in request.META and request.META["HTTP_X_REQUESTED_WITH"] == "XMLHttpRequest":
        categories = request.GET.getlist('categories[]')
        query = request.GET.get('query', '')
        projects = Item.objects.all()
        if categories and categories[0] != '':
            categories = categories[0].split(',')
            projects = projects.filter(category__title__in=categories)
        if query:
            query_words = query.split(' ')
            projects = projects.filter(title__icontains=query_words[0])
            for word in query_words[1:]:
                projects = projects.filter(title__icontains=word)

        res_projects = list(map(projects_map, projects))
        return JsonResponse(data=res_projects, safe=False)
    else:
        return JsonResponse(data={'status':'400 Bad Request'})