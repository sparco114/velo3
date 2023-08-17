from rest_framework.permissions import BasePermission

from src.bicycles.models import Bicycle
from src.logbooks.models import LogBookRecord


class IsBicycleOwner(BasePermission):

    def has_permission(self, request, view):
        bicycle_pk = view.kwargs.get('pk')
        bicycle = Bicycle.objects.get(pk=bicycle_pk)
        owner = bicycle.owner
        return owner == request.user


class IsRecordCreator(BasePermission):

    def has_permission(self, request, view):
        record_pk = view.kwargs.get('pk')
        record = LogBookRecord.objects.get(pk=record_pk)
        return record.creator == request.user
