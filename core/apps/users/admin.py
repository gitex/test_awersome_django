from django.contrib import admin

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'email',
        'last_name',
        'first_name',
        'middle_name',
    )
    list_filter = ('is_active',)
    list_display_links = ('email',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-id',)
    fieldsets = (
        (
            None,
            {
                'fields': ('password',),
            },
        ),
        (
            'Персональная информация',
            {
                'fields': ('last_name', 'first_name', 'middle_name', 'email',),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
