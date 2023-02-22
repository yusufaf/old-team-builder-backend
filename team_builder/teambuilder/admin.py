from django.contrib import admin
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'createdAt', 'updatedAt')


admin.site.register(Team, TeamAdmin)
