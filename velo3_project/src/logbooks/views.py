from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.logbooks.models import LogBookRecord
from src.logbooks.serializers import LogBookRecordSerializer


class LogBookRecordViewSet(ModelViewSet):
    queryset = LogBookRecord.objects.all()
    serializer_class = LogBookRecordSerializer
    # permission_classes = [IsAuthenticated]
