from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    following = models.ManyToManyField('self', related_name='followers', blank=True,
                                       symmetrical=False)
