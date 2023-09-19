from django.contrib import admin

from src.logbooks.models import LogBookRecord, LogBookRecordPictures


@admin.register(LogBookRecord)
class LogBookRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(LogBookRecordPictures)
class LogBookRecordPicturesAdmin(admin.ModelAdmin):
    pass
