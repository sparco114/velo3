from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# TODO: вынести функции _directory_path из всех приложений в одно место, чтоб не было повторения кода
def user_avatar_directory_path(instance, filename):
    current_datetime = str(timezone.now().replace(microsecond=0))
    file_format = filename.split('.')[-1]
    full_filename = f'{current_datetime}.{file_format}'
    return f'avatars/id_{instance.id}/{full_filename}'


class VeloUser(AbstractUser):
    """Custom user model"""

    city = models.CharField(max_length=25, blank=True, null=True)
    # TODO: настроить удаление фото из директории при удалении/изменении аватара
    avatar = models.ImageField(upload_to=user_avatar_directory_path, blank=True, null=True)


class VeloUserProfile(models.Model):
    """Users info profile (additional information about user for user's profile page)"""

    GENDER = (
        ('М', 'М'),
        ('Ж', 'Ж'),
        ('не указан', 'не указан'),
    )
    velouser = models.OneToOneField(VeloUser, on_delete=models.CASCADE)
    sex = models.CharField(max_length=9, choices=GENDER, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    # TODO: если переименовать phone на contacts, то нужно изменить max_length 
    phone = models.CharField(max_length=14, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'id {self.pk}: {self.velouser}'


@receiver(post_save, sender=VeloUser)
def create_or_update_user_profile(instance, created, **kwargs):
    if created:
        VeloUserProfile.objects.create(velouser=instance)
    # else:
    #     instance.userprofile.save()
