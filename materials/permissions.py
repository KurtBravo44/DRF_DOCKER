from rest_framework.permissions import BasePermission

from materials.models import Lesson
from user.models import UserRole


class IsOwner(BasePermission):
    message = 'You are not owner'

    def has_permission(self, request, view):
        lesson = Lesson.objects.get(pk=view.kwargs['pk'])
        if request.user == lesson.owner:
            return True


class IsModerator(BasePermission):
    message = 'You are not moderator'

    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        else:
            return False
