from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # only allow Owners of objects to use modifying HTTP methods
        return obj.User == request.user

class IsOwnerOrReadOnly_CollectionItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # only allow Owners of objects to use modifying HTTP methods
        return obj.Collection.Profile.User == request.user

class IsOwnerOrReadOnly_Profile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # only allow Owners of objects to use modifying HTTP methods
        return obj.Profile.User == request.user