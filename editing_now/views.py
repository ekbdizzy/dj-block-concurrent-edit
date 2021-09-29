from django.http import JsonResponse
from editing_now.models import EditingNow
from django.utils import timezone


def is_editing_now(request, model_name):
    try:
        editing_now_object = EditingNow.objects.get(model_name=model_name)
        return JsonResponse({'model_name': model_name,
                             'user': editing_now_object.user.username,
                             'edited_at': editing_now_object.is_updated.strftime('%d.%m.%y %H:%M')})
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
        try:
            editing_model = EditingNow.objects.select_related('user').get(model_name=model_name)
            if editing_model.user == request.user:
                editing_model.is_updated = timezone.now()
                editing_model.save()
                return JsonResponse({'model_name': "updated"})
            else:
                return JsonResponse(
                    {'alert': 'Пользователь сменился',
                     'user': editing_model.user.username}
                )
        except EditingNow.DoesNotExist:
            EditingNow.objects.create(
                model_name=model_name,
                user=request.user
            )
            return JsonResponse({'model_name': "created"})

    return JsonResponse({'error': 'method is not valid'})


def update_user_in_editing_now_model(request, model_name):
    if request.method == 'UPDATE':
        EditingNow.objects.filter(model_name=model_name).update(
            is_updated=timezone.now(), user=request.user)
        return JsonResponse({'model_name': "updated"})
    return JsonResponse({'error': 'method is not valid'})
