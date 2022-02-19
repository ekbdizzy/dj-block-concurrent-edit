from django.urls import path
from .views import is_editing_now, create_new_editing_model, update_editing_now_model, update_user_in_editing_now_model

app_name = 'locked_models'

urlpatterns = [
    path('get/<str:model_name>/', is_editing_now),
    path('create/<str:model_name>/', create_new_editing_model),
    path('update/<str:model_name>/', update_editing_now_model),
    path('update_user/<str:model_name>/', update_user_in_editing_now_model),
]
