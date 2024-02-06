from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='base@mail.ru',
            first_name='base',
            last_name='base',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password('2344')
        user.save()
