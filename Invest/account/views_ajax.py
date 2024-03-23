from django.db.models.fields.files import ImageFieldFile
from django.http import JsonResponse
from django.db.models import F, Value
from django.core import serializers
from django.db.models.functions import Concat
from django.db.models import CharField
from django.core.serializers import serialize
from invest_projects.models import Item


def delete_project(request, user_id, project_id):
    project = Item.objects.get(id=project_id)
    project.delete()

    return JsonResponse({'status':200})