from django.urls import path
from .views import locked_model_view, update_locked_model_user_view

app_name = 'locked_models'

urlpatterns = [
    path('locked_model/<str:model_name>/', locked_model_view),
    path('locked_model/<str:model_name>/user/', update_locked_model_user_view),
]
