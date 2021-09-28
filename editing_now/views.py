from django.http import JsonResponse
from editing_now.models import EditingNow
from django.utils import timezone


def is_editing_now(request, model_name):
    try:
        editing_now_object = EditingNow.objects.get(model_name=model_name)
        return JsonResponse({'model_name': model_name,
                             'user': editing_now_object.user.username})
    except EditingNow.DoesNotExist:
        return JsonResponse({'model_name': None})


def create_new_editing_model(request, model_name):
    if request.method == 'POST':
        EditingNow.objects.create(
            model_name=model_name,
            user=request.user
        )
        return JsonResponse({'model_name': model_name})


def update_editing_now_model(request, model_name):
    if request.method == 'UPDATE':
        EditingNow.objects.filter(model_name=model_name).update(
            is_updated=timezone.now())
        return JsonResponse({'model_name': "updated"})
    return JsonResponse({'error': 'method is not valid'})


def update_user_in_editing_now_model(request, model_name):
    if request.method == 'UPDATE':
        EditingNow.objects.filter(model_name=model_name).update(
            is_updated=timezone.now(), user=request.user)
        return JsonResponse({'model_name': "updated"})
    return JsonResponse({'error': 'method is not valid'})
