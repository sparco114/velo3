from rest_framework import serializers

from src.bicycles.serializers import BicycleListSerializer
from src.profiles.serializers import VeloUserSerializer
from src.logbooks.models import LogBookRecord, LogBookRecordPictures


class LogBookRecordPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogBookRecordPictures
        fields = '__all__'


class LogBookRecordSerializer(serializers.ModelSerializer):
    # bicycle = serializers.CharField(read_only=True)
    bicycle = BicycleListSerializer(read_only=True)
    # creator = serializers.CharField(read_only=True)
    creator = VeloUserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pictures = LogBookRecordPictureSerializer(many=True, required=False)

    class Meta:
        model = LogBookRecord
        exclude = ('is_published',)
