from django.http import JsonResponse
from .models import AtelierEntity
from django.shortcuts import render


def entities_list(request):
    all_entities = AtelierEntity.objects.all()
    data = list(all_entities.values('id', 'name', 'price', 'available', 'description', 'type', 'image_path'))
    return JsonResponse(data, safe=False)
