from rest_framework.viewsets import ReadOnlyModelViewSet

from src.bicycles.models import Bicycle
from src.bicycles.serializers import BicycleSerializer


class BicycleViewSet(ReadOnlyModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
    # http_method_names = ['get']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
