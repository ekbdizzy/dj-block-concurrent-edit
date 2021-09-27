from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'post_list_display.html'
