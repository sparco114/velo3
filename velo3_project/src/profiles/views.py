from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from src.profiles.models import VeloUser, VeloUserProfile
from src.profiles.serializers import VeloUserSerializer, VeloUserProfileSerializer


class VeloUserViewSet(ModelViewSet):
    queryset = VeloUser.objects.all()
    serializer_class = VeloUserSerializer


class VeloUserProfileViewSet(ModelViewSet):
    queryset = VeloUserProfile.objects.all()
    serializer_class = VeloUserProfileSerializer

