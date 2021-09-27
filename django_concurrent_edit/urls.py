from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('is_editing/', include('editing_now.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
