from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 1