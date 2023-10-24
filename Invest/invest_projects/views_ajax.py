from .models import Item, ItemImage

from django.http import JsonResponse
from django.db.models import F, Value
from django.core import serializers
from django.db.models.functions import Concat
from django.db.models import CharField


def projects_map(project):
    images_urls = [item_image.image.url for item_image in project.images.all()]

    project_dict = project.__dict__
    project_dict = {key: value for key, value in project_dict.items() if not key.startswith('_')}
    project_dict['images_urls'] = images_urls
    return project_dict


def GetAllInvestProjects(request):
    if "HTTP_X_REQUESTED_WITH" in request.META and request.META["HTTP_X_REQUESTED_WITH"] == "XMLHttpRequest":
        projects = Item.objects.all()
        res_projects = list(map(projects_map, projects))
        return JsonResponse(data=res_projects, safe=False)
    else:
        return JsonResponse(data={'status':'400 Bad Request'})