from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin, AbstractUser, User

class User(AbstractUser):
    phone = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.ImageField(upload_to='Images/', blank=True, null=True)
    is_manager = models.BooleanField(default=False)
    vk_link = models.CharField(max_length=256, blank=True, null=True)
    fb_link = models.CharField(max_length=256, blank=True, null=True)
    insta_link = models.CharField(max_length=256, blank=True, null=True)
