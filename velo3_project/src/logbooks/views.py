from rest_framework import permissions
from rest_framework import viewsets, generics

from src.bicycles.models import Bicycle
from src.logbooks.models import LogBookRecord
from src.logbooks.permissions import IsBicycleOwner, IsRecordCreator
from src.logbooks.serializers import LogBookRecordSerializer


class LogBookRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogBookRecord.objects.all()
    serializer_class = LogBookRecordSerializer


class BicycleLogBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LogBookRecordSerializer

    def get_queryset(self):
        bicycle_pk = self.kwargs.get('pk')
        queryset = LogBookRecord.objects.filter(bicycle=bicycle_pk)
        return queryset


class BicycleLogBookRecordCreateView(generics.CreateAPIView):
    permission_classes = [IsBicycleOwner]
    serializer_class = LogBookRecordSerializer

    def perform_create(self, serializer):
        bicycle_pk = self.kwargs.get('pk')  # - можно брать просто из словаря (self.kwargs['pk']), но если не будет pk, то вернется исключени, а если брать через get то вернется не исключение а просто None
        bicycle = Bicycle.objects.get(pk=bicycle_pk)
        serializer.save(bicycle=bicycle, creator=self.request.user)


class LogBookRecordUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRecordCreator]
    serializer_class = LogBookRecordSerializer

    def get_queryset(self):
        record_pk = self.kwargs.get('pk')
        queryset = LogBookRecord.objects.filter(pk=record_pk)
        return queryset



