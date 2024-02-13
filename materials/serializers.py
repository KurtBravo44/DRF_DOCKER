from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]

class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribe(self, instance):
        user = self.context['request'].user
        is_subscribed = Subscription.objects.filter(user=user,
                                                    course=instance).exists()
        return is_subscribed


    def get_lesson_count(self, instance):
        return instance.lesson_set.all().count()

    def create(self, validated_data):
        new_course = Course.objects.create(**validated_data)
        new_course.owner = self.context['request'].user
        new_course.save()
        return new_course


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'

