from django.urls import path
from rest_framework.routers import DefaultRouter

from user.apps import UserConfig
from user.views import PaymentViewSet

app_name = UserConfig.name

router = DefaultRouter()
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [

] + router.urls