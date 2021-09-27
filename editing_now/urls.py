from django.urls import path
from .views import is_editing_now

app_name = 'editing_now'

urlpatterns = [
    path('check/<str:model_name>/', is_editing_now)
]
