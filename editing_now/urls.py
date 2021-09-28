from django.urls import path
from .views import is_editing_now, update_editing_now_model

app_name = 'editing_now'

urlpatterns = [
    path('check/<str:model_name>/', is_editing_now),
    path('update/<str:model_name>/', update_editing_now_model),
]
