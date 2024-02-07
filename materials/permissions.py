from rest_framework.permissions import BasePermission

from user.models import UserRole


class IsOwner(BasePermission):
    message = 'You are not owner'

    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True
        else:
            return False


class IsModerator(BasePermission):
    message = 'You are not moderator'

    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        return False
