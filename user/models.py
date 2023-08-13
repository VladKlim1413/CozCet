from django.db import models

from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    full_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя и фамилия')
    email = models.EmailField(max_length=200, blank=False, null=True, unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    user_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Логин")
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True, verbose_name='Фото пользователя')

    def __str__(self):
        if self.full_name:
            return f'{self.full_name} {self.email}'
        return f'{self.username} {self.email}'
