import datetime

from django.http import JsonResponse
from django.shortcuts import render
from editing_now.models import EditingNow
from django.utils import timezone


def is_editing_now(request, model_name):
    editing_now_object = EditingNow.objects.get(model_name=model_name)
    print(editing_now_object)
    return JsonResponse({'model': editing_now_object.model_name})


def update_editing_now_model(request, model_name):
    if request.method == 'UPDATE':
        EditingNow.objects.filter(model_name=model_name).update(
            is_updated=timezone.now())
        return JsonResponse({'model': "updated"})
    return JsonResponse({'error': 'method is not valid'})
