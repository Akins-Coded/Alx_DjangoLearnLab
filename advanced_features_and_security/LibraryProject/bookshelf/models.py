from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.
class Book(models.Model):
    title = models.CharField (max_length=200)
    author = models.CharField (max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.author} {self.publication_year}"

    class Meta:
        permissions = (
            ("can_edit", "Can edit"),
            ("can_create", "Can create"),
            ("can_delete", "Can delete"),
            ("can_view", "Can view"),
        )

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, verbose_name="Profile Photo")

    def __str__(self):
        return self.username
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelf_profile')

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email, password, and all the required fields.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)