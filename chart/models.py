from django.db import models
import os
from django.conf import settings
# Create your models here.

class Chart(models.Model):
    chart_rank = models.PositiveSmallIntegerField(null=True, blank = True, verbose_name = "우선순위")
    chart_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="작성자")
    chart_title = models.CharField(max_length=128, verbose_name="차트 이름")
    chart_url = models.TextField(verbose_name = "차트 URL")
    chart_register = models.DateTimeField(auto_now=True, verbose_name="등록 시간")

    def __str__(self):
        return self.chart_title
    
    class Meta:
        db_table = "차트설정 메뉴"
        verbose_name = "차트설정 메뉴"
        verbose_name_plural = "차트설정 메뉴"