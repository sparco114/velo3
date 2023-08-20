from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from src.bicycles.models import Bicycle
from src.bicycles.permissions import IsOwner
from src.bicycles.serializers import BicycleSerializer


class BicycleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
    # http_method_names = ['get']


class MyBicycleListViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BicycleSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Bicycle.objects.filter(owner=user)
        return queryset


class MyBicycleCreateViewSet(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BicycleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MyBicycleUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = BicycleSerializer

    def get_queryset(self):
        bicycle_pk = self.kwargs.get('pk')
        queryset = Bicycle.objects.filter(pk=bicycle_pk)
        return queryset


# """перенес эту функциональность в logbooks/views"""
# class TEST_MET(viewsets.ReadOnlyModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = BicycleSerializer
#     queryset = Bicycle.objects.all()
#
#     # @action(methods=['get'], detail=False)  # на случай если используются роутеры
#     def logbook(self, request, pk=None):
#         logs = LogBookRecord.objects.filter(bicycle=pk)
#         ser = LogBookRecordSerializer(logs, many=True)
#         return Response({'logs': ser.data})


def main_page(request):
    return render(request, 'index.html')


def bicycles_list(request):
    return render(request, 'bicycles.html')
