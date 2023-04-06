from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Login')
    user_name = models.CharField(max_length=255, verbose_name='User name')
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    phone = models.CharField(max_length=20, verbose_name='User phone')
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True, verbose_name='Profile photo')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
