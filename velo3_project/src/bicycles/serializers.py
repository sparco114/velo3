from rest_framework.serializers import ModelSerializer

from src.bicycles.models import Bicycle


class BicycleSerializer(ModelSerializer):
    class Meta:
        model = Bicycle
        fields = '__all__'
