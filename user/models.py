from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null':True, 'blank':True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    phone = models.IntegerField(verbose_name='телефон', **NULLABLE)

    is_superuser = models.BooleanField(default=False, verbose_name='администратор')
    is_staff = models.BooleanField(default=False, verbose_name='сотрудник')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
