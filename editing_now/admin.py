from django.contrib import admin
from .models import EditingNow


@admin.register(EditingNow)
class EditingNowAdmin(admin.ModelAdmin):
    list_display = ('model_name',
                    'user',
                    'is_created',
                    'is_updated',)
