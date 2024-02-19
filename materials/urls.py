from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView, \
    SubscriptionListAPIView, PaymentCreateAPIView

app_name = MaterialsConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('courses/<int:pk>/sub/', SubscriptionCreateAPIView.as_view(), name='sub_create'),
    path('sub/list/', SubscriptionListAPIView.as_view(), name='sub_list'),
    path('courses/<int:pk>/unsub/', SubscriptionDestroyAPIView.as_view(), name='sub_delete'),

    path('courses/buy/<int:pk>/', PaymentCreateAPIView.as_view(), name='buy_course'),
]

urlpatterns += router.urls