from rest_framework import serializers

from src.bicycles.serializers import BicycleSerializer
from src.logbooks.models import LogBookRecord


class LogBookRecordSerializer(serializers.ModelSerializer):
    # bicycle = serializers.CharField(read_only=True)
    bicycle = BicycleSerializer()
    creator = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y")
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LogBookRecord
        exclude = ('is_published', )
