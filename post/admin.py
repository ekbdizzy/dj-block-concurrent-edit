from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'edited_at',)
    readonly_fields = ('created_at', 'edited_at',)
