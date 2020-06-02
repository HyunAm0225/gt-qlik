from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'cart_id',
    )
admin.site.register(Cart,CartAdmin)