from django.contrib import admin

from src.logbooks.models import LogBookRecord


@admin.register(LogBookRecord)
class LogBookRecordAdmin(admin.ModelAdmin):
    pass
