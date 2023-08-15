from rest_framework import serializers
from src.bicycles.models import Bicycle


class BicycleSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Bicycle
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user
    #     return super().create(validated_data)

