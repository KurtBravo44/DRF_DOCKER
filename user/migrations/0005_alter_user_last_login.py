# Generated by Django 4.2.10 on 2024-02-26 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_payment_amount_alter_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='последняя авторизация'),
        ),
    ]