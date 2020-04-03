from django.contrib import admin

from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','dept_name','rank','email')
    search_fields = ['name']
admin.site.register(User,UserAdmin)