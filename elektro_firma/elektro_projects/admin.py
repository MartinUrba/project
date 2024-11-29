from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'customer', 'assigned_persons_list')  # Opravené sloupce
    search_fields = ('name',)  # Vyhledávání podle názvu projektu
    ordering = ('name',)  # Seřadí projekty podle názvu

    def assigned_persons_list(self, obj):
        return ", ".join([person.name for person in obj.assigned_persons.all()])
    assigned_persons_list.short_description = 'Assigned Persons'

# Zaregistruj model Project do admin rozhraní
admin.site.register(Project, ProjectAdmin)