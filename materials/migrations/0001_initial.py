# Generated by Django 5.0.1 on 2024-01-22 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='materials/course/', verbose_name='превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='materials/lesson/', verbose_name='превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('link', models.TextField(verbose_name='ссылка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
