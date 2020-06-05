from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import SetPasswordForm

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
    name = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={
            "placeholder" : "이름 입력"
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
        fields = ['username','password1','password2','name','email','dept_name','rank','gender',]

    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationform, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
        label="아이디",
        widget = forms.TextInput(attrs={
            "placeholder" : "사용자 아이디",
            'readonly' : 'readonly'
        })
    )
    name = forms.CharField(
        label="이름",
        widget = forms.TextInput(attrs={
            "placeholder" : "이름 입력",
            'readonly' : 'readonly'
        })
    )
    dept_name = forms.CharField(
        label="부서 이름",
        widget = forms.TextInput(attrs={
            "placeholder" : "부서 이름"
        })
    )
    rank = forms.CharField(
        label="직급",
        widget = forms.TextInput(attrs={
            "placeholder" : "직급"
        })
    )
    email = forms.EmailField(
        label="이메일",
        widget = forms.EmailInput(attrs={
            "placeholder" : "이메일 입력",
            'readonly' : 'readonly'
        })

    )
    class Meta:
        model = get_user_model()
        fields = ['username','name','email','dept_name','rank','gender',]
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            # self.fields[field].label=''


# 비밀번호 찾기
class RecoveryPwForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput,)
    name = forms.CharField(
        widget=forms.TextInput,)
    email = forms.EmailField(
        widget=forms.EmailInput,)

    class Meta:
        fields = ['username', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_id',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_name',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email',
        })

# 인증번호 입력 후 사용자의 비밀번호 변경
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })

