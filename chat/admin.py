from django.contrib import admin

from .models import Group
# Register your models here.

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'get_users_of_group')


    def get_users_of_group(self, obj):
        users = ", ".join([user.username for user in obj.members.all()])
        return users