from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsVerifiedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and getattr(request.user, 'is_verified', False)

class AllowOnlyPost(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'


class ReadOrDeleteOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'DELETE']


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsInGroup(permissions.BasePermission):
    def __init__(self, group_name):
        self.group_name = group_name

    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name=self.group_name).exists()



