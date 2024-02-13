from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView, \
    SubscriptionListAPIView

app_name = MaterialsConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('courses/<int:pk>/subs/', SubscriptionCreateAPIView.as_view(), name='course_subs'),
    path('courses/subs/list/', SubscriptionListAPIView.as_view(), name='course_subs_list'),
    path('courses/<int:pk>/subs/delete/<int:subscription_pk>/', SubscriptionDestroyAPIView.as_view(), name='course_subs_delete'),

]

urlpatterns += router.urls