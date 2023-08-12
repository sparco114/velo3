from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from src.bicycles.models import Bicycle
from src.bicycles.serializers import BicycleSerializer


class BicycleViewSet(ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
