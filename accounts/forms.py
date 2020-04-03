from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms 
from .models import User

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
    dept_name = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={
            "placeholder" : "부서 이름"
        })
    )
    rank = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={
            "placeholder" : "직급"
        })
    )
    email = forms.EmailField(
        label="",
        widget = forms.EmailInput(attrs={
            "placeholder" : "이메일 입력"
        })

    )

    class Meta:
        model = get_user_model()
        fields = ['username','password1','password2','email','dept_name','rank','gender',]
    