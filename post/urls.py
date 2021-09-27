from django.urls import path
from .views import PostsListView

app_name = 'post'

urlpatterns = [
    path('', PostsListView.as_view())
]
