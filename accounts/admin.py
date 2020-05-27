from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import User
# Register your models here.
class UserAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name','dept_name','rank','email')
    search_fields = ['name']
admin.site.register(User,UserAdmin)