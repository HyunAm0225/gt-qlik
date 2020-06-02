from django.db import models
from chart.models import Chart

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = '장바구니'
        ordering = ['date_added']
    
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    class Meta:
        db_table : '장바구니 차트'
    
    def __str__(self):
        return self.chart
    