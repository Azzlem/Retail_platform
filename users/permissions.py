from rest_framework.permissions import BasePermission


class IsOwnerOrStaffUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().user


class IsOwnerOrStaffProduct(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner


class IsOwnerOrStaffProductProvider(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().author



