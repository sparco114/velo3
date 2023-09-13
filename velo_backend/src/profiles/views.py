from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from src.profiles.models import VeloUser
from src.profiles.serializers import VeloUserSerializer


class VeloUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VeloUser.objects.all()
    serializer_class = VeloUserSerializer


class MyVeloUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VeloUserSerializer

    def get_object(self):
        return self.request.user

