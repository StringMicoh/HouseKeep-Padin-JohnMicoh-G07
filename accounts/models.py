from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = 'USER', 'Household User'
        ADMIN = 'ADMIN', 'Administrator'

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.username
