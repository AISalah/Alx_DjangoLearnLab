from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', related_name='following', blank=True, symmetrical=False)
