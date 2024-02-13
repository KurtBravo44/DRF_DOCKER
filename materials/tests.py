from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson, Subscription
from user.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            email='base@mail.ru',
            password='2344',
            is_active=True
        )

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='TEST',
            description='TEST DESC',
            owner=self.user,
        )


    def test_create_lesson(self):
        """Create lesson"""

        data = {
            'title': 'TEST',
            'description': 'TEST DESC',
            'course': self.course.pk,
            'owner': self.user.pk,
            'link': 'https://www.youtube.com/watch?v=gzXxxamxvtc'
        }
        response = self.client.post(
            reverse('materials:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_lesson(self):
        """test list"""
        response = self.client.get(
            reverse('materials:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}
        )

    def test_update_lesson(self):
        lesson = Lesson.objects.create(
            course=self.course,
            title='TEST',
            link='https://www.youtube.com/watch?v=gzXxxamxvtc',
            owner=self.user,
            pk=2
        )
        print(lesson.owner)
        data = {
            'title': 'New_TITLE',
            'course': self.course.pk,
            'owner': self.user.pk,
            'link': 'https://www.youtube.com/watch?v=asfas',

        }

        response = self.client.put(
            reverse('materials:lesson_update', kwargs={'pk': lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """delete lesson"""
        lesson = Lesson.objects.create(
            course=self.course,
            title='TEST',
            link='https://www.youtube.com/watch?v=gzXxxamxvtc',
            owner=self.user,
            pk=2
        )

        response = self.client.delete(
            reverse('materials:lesson_delete', kwargs={'pk': lesson.pk})
        )

class SubscripeTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            email='base@mail.ru',
            password='2344',
            is_active=True
        )

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='TEST',
            description='TEST DESC',
            owner=self.user,
        )

    def test_create_subs(self):
        """Create subs"""

        data = {
            'user': self.user.pk,
            'course': self.course.pk
        }
        response = self.client.post(
            reverse('materials:course_subs', kwargs={'pk': self.course.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_subs(self):
        """create subs"""
        response = self.client.get(
            reverse('materials:course_subs_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_subs(self):
        """delete subs"""
        subs= Subscription.objects.create(
            course=self.course,
            user=self.user
        )

        response = self.client.delete(
            reverse('materials:course_subs_delete', kwargs={'pk': self.course.pk, 'subscription_pk': subs.pk})
        )

