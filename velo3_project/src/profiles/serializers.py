from rest_framework.serializers import ModelSerializer

from src.profiles.models import VeloUser, VeloUserProfile


class VeloUserSerializer(ModelSerializer):
    class Meta:
        model = VeloUser
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'city', 'avatar')


class VeloUserProfileSerializer(ModelSerializer):
    class Meta:
        model = VeloUserProfile
        fields = '__all__'
