from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        bicycle = view.get_object()
        return request.user == bicycle.owner

