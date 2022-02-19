from django.contrib import admin
from .models import LockedModel


@admin.register(LockedModel)
class LockedModelAdmin(admin.ModelAdmin):
    list_display = ('model_name',
                    'user',
                    'is_created',
                    'is_updated',)
