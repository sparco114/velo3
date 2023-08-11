from django.contrib import admin

from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from src.profiles.models import VeloUser


class VeloUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'city', 'first_name', 'last_name', 'is_staff') #опционально. переопределяем поля, которые отображаются в админке, чтобы можно было изменять.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'city')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'city'),
        }),
    )


admin.site.register(VeloUser, VeloUserAdmin)
