from .models import Cart, CartItem
from django.contrib.auth.models import User


def counter(request):
    if 'admin' in request.path:
        return {}

    else:
        try:
            cart = Cart.objects.filter(user_id=User)
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
        
        except Cart.DoesNotExist:
            cart_items = 0
        return dict(cart_items = cart_items)