from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson
from django.utils.translation import gettext_lazy as _
NULLABLE = {'null': True, 'blank': True}

class UserRole(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    phone = models.IntegerField(verbose_name='телефон', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRole.choices, default=UserRole.MEMBER)

    is_superuser = models.BooleanField(default=False, verbose_name='администратор')
    is_staff = models.BooleanField(default=False, verbose_name='сотрудник')
    is_active = models.BooleanField(default=False, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


payment_methods = (
    ('cash', 'наличные'),
    ('transfer', 'перевод'),
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    date = models.DateField(auto_now_add=True, verbose_name='дата')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', blank=True, null=True)
    amount = models.IntegerField(verbose_name='сумма')
    method = models.CharField(max_length=8, choices=payment_methods, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user}: {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-date',)
