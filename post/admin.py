from django.contrib import admin
from .models import Post
from editing_now.models import EditingNow
from django.shortcuts import render


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'edited_at',)
    readonly_fields = ('created_at', 'edited_at',)

    change_form_template = 'concurrency_change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):

        # Если модель уже редактируется, перенаправляем на шаблон, который сообщает, что модель недоступна
        current_edit_object_name = f'{self.model._meta.model_name}_{object_id}'
        try:
            editing_model = EditingNow.objects.get(model_name=current_edit_object_name)
            if editing_model.user != request.user:
                current_model = self.model.objects.get(id=object_id)
                return render(request, 'model_is_unavailable_to_edit.html',
                              context={'model': current_model, 'user': request.user})
        except EditingNow.DoesNotExist:
            pass

        # Добавляем модель в список редактируемых
        EditingNow.objects.update_or_create(
            model_name=current_edit_object_name,
            user=request.user
        )

        extra_context = {
            "editing_model": current_edit_object_name,
        }
        return super(PostAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        # При сохранении объекта удаляем запись из CurrentEdit
        current_edit_object_name = f'{self.model._meta.model_name}_{obj.id}'
        EditingNow.objects.filter(model_name__exact=current_edit_object_name).delete()
        obj.save()
