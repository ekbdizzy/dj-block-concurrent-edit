from django.http import JsonResponse
from django.shortcuts import render
from editing_now.models import EditingNow


def is_editing_now(request, model_name):
    editing_now_object = EditingNow.objects.get(model_name=model_name)
    print(editing_now_object)

    return JsonResponse({'model': editing_now_object.model_name})
