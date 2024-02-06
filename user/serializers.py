from django.views.generic import CreateView
from rest_framework import serializers

from user.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RegisterView(CreateView):
    model = User
