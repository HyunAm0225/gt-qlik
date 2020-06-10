from django.db import models
import os
from django.conf import settings
from django.db import models


# Create your models here.

class Menu(models.Model):
    menu_rank = models.PositiveSmallIntegerField(null=True, blank = True, verbose_name = "우선순위")
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length = 128, verbose_name = '메뉴 이름')
    url = models.TextField(verbose_name='URL')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    
    def __str__(self):
        return self.title

    class Meta:
        db_table = '화면설정 메뉴'
        verbose_name = '화면설정 메뉴'
        verbose_name_plural = '화면설정 메뉴'