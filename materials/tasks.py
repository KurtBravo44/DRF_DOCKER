from celery import shared_task
from django.utils import timezone

from materials.services import send_mail
from user.models import User


@shared_task
def send_mail_about_update(user_email):
    send_mail(
        _to_mail=user_email,
        _subject='LMS',
        _message='Курс, на который вы подписались, обновился!\n'
                 'Проверьте изменения.'
    )
    print('сообщение отправлено')

@shared_task
def diactivate_user():
    today = timezone.now()
    users_list = User.objects.all()

    for user in users_list:
        days_diff = (today - user.last_login).days
        if days_diff > 30:
            user.is_active = False
            user.save()




