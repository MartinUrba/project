from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'customer', 'get_assigned_to']

    def get_assigned_to(self, obj):
        return ", ".join([user.username for user in obj.assigned_to.all()])
    get_assigned_to.short_description = 'Assigned To'

admin.site.register(Project, ProjectAdmin)
