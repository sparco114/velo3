from rest_framework import serializers

from src.bicycles.serializers import BicycleListSerializer
from src.profiles.serializers import VeloUserSerializer
from src.logbooks.models import LogBookRecord



class LogBookRecordSerializer(serializers.ModelSerializer):
    # bicycle = serializers.CharField(read_only=True)
    bicycle = BicycleListSerializer(read_only=True)
    # creator = serializers.CharField(read_only=True)
    creator = VeloUserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LogBookRecord
        exclude = ('is_published', )


# class LogBookRecordCreateSerializer(serializers.ModelSerializer):
#     # bicycle = serializers.CharField(read_only=True)
#     bicycle = BicycleListSerializer(read_only=True)
#     creator = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)
#     # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = LogBookRecord
#         exclude = ('is_published', )