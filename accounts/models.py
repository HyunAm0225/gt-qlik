from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=30,blank=True)
    email = models.EmailField(max_length=254, unique = True, verbose_name = 'email address')
    dept_name = models.CharField(max_length=50,blank=True)
    rank = models.CharField(max_length=20,blank=True)
    auth = models.CharField(max_length=10, verbose_name="인증번호", null=True)
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    CHOICES_GENDER = (
        (GENDER_MALE,'남성'),
        (GENDER_FEMALE,'여성'),
    )
    gender = models.CharField(max_length = 10, choices=CHOICES_GENDER)
