from django.conf import settings
from django.db import models



NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='materials/course/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='materials/lesson/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.TextField(verbose_name='ссылка', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'Подписка {self.user} : {self.course}'

    class Meta:

        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
