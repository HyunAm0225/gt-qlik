from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms 

class CustomUserCreationform(UserCreationForm):
    username = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={
            "placeholder" : "사용자 아이디"
        })
    )
    password1 = forms.CharField(
        label="",
        widget = forms.PasswordInput(attrs={
            "placeholder" : "비밀번호(8자이상)"
        })
    )
    password2 = forms.CharField(
        label="",
        widget = forms.PasswordInput(attrs={
            "placeholder" : "비밀번호 확인"
        })
    )

    class Meta:
        model = get_user_model()
        fileds = ['username','password1','password2',]
    