from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class LockedModel(models.Model):
    model_name = models.CharField(max_length=300, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(default=timezone.now)
