from django.contrib import admin

# Register your models here.
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    default django-admin
    User Profile admin
    """
    list_display = ('user', 'birthday', 'gender', 'mobile', 'email', 'authority')

    fieldsets = (
        ('基本信息', {'fields': ('user', 'gender', 'birthday', 'authority')}),
        ('联系方式', {'fields': ('mobile', 'email')}),
    )
