from django.core.management import BaseCommand

from materials.models import Course
from user.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():
            pm = Payment.objects.create(user=user, course=Course.objects.get(pk=2), amount=500, method='cash')
            pm.save()
