from django.contrib import admin
from .models import Project

# Register your models here.


# Tady můžeš přidat vlastní nastavení admin rozhraní pro model Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'assigned_to')  # Sloupce, které se zobrazí v seznamu
    search_fields = ('name', 'assigned_to')  # Možnost vyhledávat podle názvu projektu a přidělené osoby
    ordering = ('name',)  # Seřadí projekty podle data začátku

# Zaregistruj model Project do admin rozhraní
admin.site.register(Project, ProjectAdmin)
