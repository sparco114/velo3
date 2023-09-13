from django.contrib import admin
from src.bicycles.models import Bicycle


@admin.register(Bicycle)
class BicycleAdmin(admin.ModelAdmin):
    pass
