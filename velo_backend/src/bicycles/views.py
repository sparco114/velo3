from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from src.bicycles.models import Bicycle
from src.bicycles.permissions import IsOwner
from src.bicycles.serializers import BicycleListSerializer, BicycleDetailSerializer


class BicycleListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BicycleListSerializer
    # http_method_names = ['get']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['owner']
    ordering_fields = ['id']

    def get_queryset(self):
        amount_first = self.request.query_params.get('first')
        amount_last = self.request.query_params.get('last')
        amount_random = self.request.query_params.get('random')

        if amount_first:
            queryset = Bicycle.objects.order_by('id')[:int(amount_first)]
        elif amount_last:
            queryset = Bicycle.objects.order_by('-id')[:int(amount_last)]
        elif amount_random:
            queryset = Bicycle.objects.order_by('?')[:int(amount_random)]
        else:
            queryset = Bicycle.objects.all()
        # TODO: добавить условие, чтобы возвращались только активные (не бывшие) велосипеды
        return queryset


class BicycleDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BicycleDetailSerializer

    def get_queryset(self):
        bicycle_pk = self.kwargs.get('pk')
        queryset = Bicycle.objects.filter(pk=bicycle_pk)
        return queryset


class MyBicycleListViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BicycleListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Bicycle.objects.filter(owner=user)
        return queryset


class MyBicycleCreateViewSet(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BicycleListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MyBicycleUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = BicycleListSerializer

    def get_queryset(self):

        # TODO: !! Принт срабатывает два раза, уточнить или запрос из BicycleEditView.vue приходит два раза,
        #  или на бэке что-то отрабатывает некорректно.
        #  А так же переписать это на get_object
        print(f"Received data: {self.request.data}")

        bicycle_pk = self.kwargs.get('pk')
        queryset = Bicycle.objects.filter(pk=bicycle_pk)
        return queryset
