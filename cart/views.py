from django.shortcuts import render, redirect
from chart.models import Chart
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    print("카트 이름 : ", cart)
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,chart_id):
    chart = Chart.objects.get(id=chart_id)
    print("차트 이름 : ", chart)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(chart=chart, cart=cart)
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            chart = chart,
            cart = cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request,cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items))