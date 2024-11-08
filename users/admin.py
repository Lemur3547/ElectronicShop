from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация модели пользователя в админке"""
    fields = ('first_name', 'last_name', 'patronymic', 'email', 'phone')
    list_display = ('first_name', 'last_name', 'patronymic', 'email', 'phone', 'is_active')
