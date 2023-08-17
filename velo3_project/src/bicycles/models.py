from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from src.profiles.models import VeloUser


def bicycle_pictures_directory_path(instance, filename):
    current_datetime = str(timezone.now().replace(microsecond=0))
    file_format = filename.split('.')[-1]
    full_filename = f'{current_datetime}.{file_format}'
    return f'bicycles/id_{instance.id}/{full_filename}'


class Bicycle(models.Model):
    WHEEL_SIZES = (
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
        ('24', '24'),
        ('26', '26'),
        ('27.5', '27.5'),
        ('28', '28'),
        ('29', '29'),
        ('36', '36'),
    )

    owner = models.ForeignKey(VeloUser, on_delete=models.CASCADE, related_name='bicycles')
    bicycle_name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=35, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True,
                                       validators=[
                                           MaxValueValidator(timezone.now().year,
                                                             message='Дата выпуска не может быть в будущем'),
                                           MinValueValidator(1817,
                                                             message='Первый велосипед изобретен в 1817 году.')
                                       ])
    # TODO: валидаторы для release_year и purchase_year вынести в один, чтоб не было копипаста
    wheel_size = models.CharField(max_length=4, blank=True, null=True, choices=WHEEL_SIZES)
    frame_material = models.CharField(max_length=35, blank=True, null=True)
    purchase_year = models.IntegerField(blank=True, null=True,
                                        validators=[
                                            MaxValueValidator(timezone.now().year,
                                                              message='Дата покупки не может быть в будущем'),
                                            MinValueValidator(1817,
                                                              message='Первый велосипед изобретен в 1817 году.')
                                        ])
    price = models.PositiveIntegerField(blank=True, null=True)
    is_former = models.BooleanField(default=False)
    about = models.TextField(blank=True, null=True)
    pictures = models.ImageField(blank=True, null=True, upload_to=bicycle_pictures_directory_path)

    def __str__(self):
        return f'id {self.pk}: {self.bicycle_name}'
