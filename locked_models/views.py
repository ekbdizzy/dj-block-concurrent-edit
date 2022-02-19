import http.client
from http import HTTPStatus

from django.http import JsonResponse
from django.utils import timezone

from locked_models.models import LockedModel


def locked_model_view(request, model_name):
    try:
        locked_model = LockedModel.objects.select_related('user').get(model_name=model_name)
    except LockedModel.DoesNotExist:
        locked_model = None

    if request.method == 'GET':
        if locked_model:
            return JsonResponse({'model_name': model_name,
                                 'user': locked_model.user.username,
                                 'edited_at': locked_model.is_updated.strftime('%d.%m.%y %H:%M')},
                                status=HTTPStatus.OK)
        return JsonResponse({'model_name': None}, status=http.client.NOT_FOUND)

    if request.method == 'POST':
        locked_model = LockedModel.objects.create(model_name=model_name, user=request.user)
        return JsonResponse({'model_name': locked_model.model_name}, status=HTTPStatus.CREATED)

    if request.method == 'PATCH':
        try:
            locked_model = LockedModel.objects.select_related('user').get(model_name=model_name)
            if locked_model.user == request.user:
                locked_model.is_updated = timezone.now()
                locked_model.save()
                return JsonResponse({'model_name': "updated"}, status=HTTPStatus.OK)
            else:
                return JsonResponse(
                    {'alert': 'Пользователь сменился',
                     'user': locked_model.user.username},
                    status=HTTPStatus.ACCEPTED
                )
        except LockedModel.DoesNotExist:
            LockedModel.objects.create(model_name=model_name, user=request.user)
            return JsonResponse({'model_name': model_name}, status=HTTPStatus.CREATED)

    return JsonResponse({'error': 'Method is not allowed'}, status=HTTPStatus.METHOD_NOT_ALLOWED)


def update_locked_model_user_view(request, model_name):
    if request.method == 'PUT':
        LockedModel.objects.filter(model_name=model_name).update(
            is_updated=timezone.now(), user=request.user)
        return JsonResponse({'model_name': model_name,
                             'user': request.user.username},
                            status=HTTPStatus.ACCEPTED)
    return JsonResponse({'error': 'Method is not allowed'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
