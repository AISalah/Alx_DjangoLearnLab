from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()



class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    # This now correctly links to whichever user model is active
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

