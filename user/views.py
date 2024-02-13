# from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView

from user.models import Payment
from user.serializers import PaymentSerializer, UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('course', 'lesson', 'method',)
    ordering_fields = ('date',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


