from django.contrib.auth.models import AbstractUser
from django.db import models


class VeloUser(AbstractUser):
    """Custom user model"""
    city = models.CharField(max_length=25, blank=True, null=True)
    # TODO: настроить верную директорию
    avatar = models.ImageField(upload_to=f'avatars/%Y/%m/%d', blank=True, null=True)

