from django.contrib import admin
from .models import CartItem,Cart

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'chart',
        'cart'
    )
admin.site.register(CartItem,CartItemAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

admin.site.register(Cart,CartAdmin)
