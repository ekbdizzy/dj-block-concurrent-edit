from django.apps import AppConfig


class LockedModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locked_models'
