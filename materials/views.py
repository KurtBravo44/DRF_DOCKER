# from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, serializers, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscription
from materials.paginators import LessonCoursePaginator
from materials.permissions import IsOwner, IsModerator
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer, PaymentSerializer
from user.models import Payment


class CourseViewSet(viewsets.ModelViewSet):
    """ ViewSet for course """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LessonCoursePaginator

    def get_permissions(self):
        if self.action == 'update':
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonCoursePaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Создает подписку ориентируясь на выбранный курс, указанный в адресе,
    а также, если подписка уже есть, он не создает новую"""
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        course_id = self.kwargs.get('pk')
        course = Course.objects.get(pk=course_id)

        if Subscription.objects.filter(user=self.request.user, course=course).exists():
            raise serializers.ValidationError("Эта подписка уже существует!")

        else:
            new_sub = serializer.save()
            new_sub.user = self.request.user
            new_sub.course = course
            new_sub.save()


class SubscriptionListAPIView(generics.ListAPIView):
    """Показывает подписки текущего пользователя"""
    serializer_class = SubscriptionSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(user=user)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Здесь я удаляю подписку авторизованного пользователя
    Ему необходимо указать pk подписки для удаления"""

    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk')
        user_id = self.request.user.pk

        subscription = Subscription.objects.get(course_id=course_id, user_id=user_id)

        if self.request.user != subscription.user:
            raise serializers.ValidationError('Это не ваша подписка')
        else:
            self.perform_destroy(subscription)
            return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course_id = self.kwargs.get('pk')
        course = Course.objects.get(pk=course_id)
        user = self.request.user

        if Payment.objects.filter(user=self.request.user, course=course).exists():
            raise serializers.ValidationError("Этот платёж уже существует!")

        else:
            new_pay = serializer.save(
                user=user,
                course=course,
                amount=int(course.price) * 100,
                method='перевод'
            )