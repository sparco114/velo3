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

        # TODO: проверить насколько корректный приходит запрос, похоже что поля для velouser_profile
        #  приходят в двух форматах: velouser_profile[phone] и velouser_profile.phone одновременно
        print(f"Received data: {self.request.data}")

        return self.request.user

