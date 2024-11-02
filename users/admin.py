from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'patronymic', 'email', 'phone')
    list_display = ('first_name', 'last_name', 'patronymic', 'email', 'phone', 'is_active')
# admin.site.register(User)
