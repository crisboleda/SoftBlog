from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession', 'picture')
    readonly_fields = ('created', 'updated')
    search_fields = ('first_name', 'last_name')
