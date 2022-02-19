from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', include('locked_models.urls')),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
