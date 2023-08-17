from rest_framework.serializers import ModelSerializer

from src.profiles.models import VeloUser, VeloUserProfile


class VeloUserProfileSerializer(ModelSerializer):
    class Meta:
        model = VeloUserProfile
        exclude = ('velouser', 'id')


class VeloUserSerializer(ModelSerializer):
    velouser_profile = VeloUserProfileSerializer(source='velouserprofile', read_only=False)
    # velouserprofile это поле которое автоматически создается в модели VeloUser, как обратная ссылка.
    # Можно присвоить ему любое имя, указав в связанном
    # поле velouser модели VeloUserProfile аргумент related_name

    # sex = serializers.CharField(source='velouserprofile.sex')
    # birthday = serializers.DateField(source='velouserprofile.birthday')
    # phone = serializers.CharField(source='velouserprofile.phone')
    # about = serializers.CharField(source='velouserprofile.about')

    class Meta:
        model = VeloUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'city', 'avatar',
                  # 'sex',
                  'velouser_profile',
                  )

    def update(self, instance, validated_data):
        velouserprofile_data = validated_data.pop('velouserprofile', {}) # внутри сериализатора используется название поля по умолчанию, и а мое название velouser_profile будет использовано только как "алиас" для доступа к связанной модели
        for attr, value in velouserprofile_data.items():
            setattr(instance.velouserprofile, attr, value)
        instance.velouserprofile.full_clean() # проверка на соответствие choice на уровне модели
        instance.velouserprofile.save()
        return super().update(instance, validated_data)
