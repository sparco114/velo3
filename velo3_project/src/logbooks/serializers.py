from rest_framework.serializers import ModelSerializer

from src.logbooks.models import LogBookRecord


class LogBookRecordSerializer(ModelSerializer):
    class Meta:
        model = LogBookRecord
        exclude = ('is_published', )
