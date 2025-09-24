from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin


class IsAdmin(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_admin


class IsUser(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_user


class IsAdminOrIsApplicationOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.is_admin or obj.applicant == request.user)
