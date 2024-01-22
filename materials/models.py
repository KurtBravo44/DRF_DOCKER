from django.db import models

from user.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='materials/course/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание', **NULLABLE)

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

