from rest_framework import serializers
from src.bicycles.models import Bicycle
from src.profiles.serializers import VeloUserSerializer


class BicycleListSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Bicycle
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user
    #     return super().create(validated_data)


class BicycleDetailSerializer(serializers.ModelSerializer):
    owner = VeloUserSerializer()

    class Meta:
        model = Bicycle
        fields = '__all__'
