from django.contrib import admin
from .models import Menu

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'menu_rank',
        'writer',
        'title',
        'url',
    )
    search_fields = ('menu_rank','title','writer',)

admin.site.register(Menu,MenuAdmin)
