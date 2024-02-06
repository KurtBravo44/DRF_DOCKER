from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator@mail.ru',
            first_name='moderator',
            last_name='moderatorov',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        user.set_password('2344')
        user.save()
