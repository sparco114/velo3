from django.db import models
from django.utils import timezone

from src.bicycles.models import Bicycle
from src.profiles.models import VeloUser


# TODO: откорректировать пути сохранения во всех моделях, чтоб было по типу media/пользователь/вело/запись
def logbook_record_pictures_directory_path(instance, filename):
    current_datetime = str(timezone.now().replace(microsecond=0))
    file_format = filename.split('.')[-1]
    full_filename = f'{current_datetime}.{file_format}'
    return f'logbook_records/id_{instance.id}/{full_filename}'


class LogBookRecord(models.Model):
    CATEGORIES = (
        ('руль', 'руль'),
        ('вилка', 'вилка'),
        ('система переклчения', 'система переклчения'),
        ('звезды', 'звезды'),
        ('тормоза', 'тормоза'),
        ('седло', 'седло'),
        ('педали', 'педали'),
        ('обода', 'обода'),
        ('покрышки', 'покрышки'),
        ('аксессуары', 'аксессуары'),
        ('рама', 'рама'),
        ('поломка', 'поломка'),
        ('плановое ТО', 'плановое ТО'),
        ('покупка велосипеда', 'покупка велосипеда'),
        ('покупка велосипеда', 'покупка велосипеда'),
        ('другое', 'другое'),
    )

    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE, related_name='logbook_records')
    header = models.CharField(max_length=100)
    text = models.TextField()
    mileage = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='другое')
    pictures = models.ImageField(blank=True, null=True, upload_to=logbook_record_pictures_directory_path)
    creator = models.ForeignKey(VeloUser, on_delete=models.CASCADE, related_name='created_logbook_records')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'id {self.pk}: {self.header}'
