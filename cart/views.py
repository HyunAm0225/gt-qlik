from django.shortcuts import render, redirect, get_object_or_404
from chart.models import Chart
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


def add_cart(request,chart_id):
    chart = Chart.objects.get(id=chart_id)

    try:
        cart = Cart.objects.get(user=request.user, cart_id= request.user.cart_id)
        
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, cart_id= request.user.cart_id)
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
        cart = Cart.objects.get(user=request.user, cart_id= request.user.cart_id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items))


def cart_remove(request,chart_id):
    print("remove 카트할때",request.user.cart_id)
    cart = Cart.objects.get(user=request.user, cart_id= request.user.cart_id)
    chart = get_object_or_404(Chart, id=chart_id)
    cart_item = CartItem.objects.get(chart=chart, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
