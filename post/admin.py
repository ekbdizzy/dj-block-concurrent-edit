from django.contrib import admin
from .models import Post
from locked_models.models import LockedModel


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'edited_at',)
    readonly_fields = ('created_at', 'edited_at',)

    change_form_template = 'concurrency_change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        locked_model_name = f'{self.model._meta.model_name}_{object_id}'
        extra_context = {'locked_model_name': locked_model_name}
        return super(PostAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        # При сохранении объекта удаляем запись из LockedModel
        current_edit_object_name = f'{self.model._meta.model_name}_{obj.id}'
        LockedModel.objects.filter(model_name__exact=current_edit_object_name).delete()
        obj.save()
