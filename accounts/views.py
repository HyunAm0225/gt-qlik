from django.shortcuts import render
from .forms import CustomUserCreationform, CustomUserChangeForm, RecoveryPwForm, CustomSetPasswordForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib import auth
from django.core.serializers.json import DjangoJSONEncoder
from requests_ntlm import HttpNtlmAuth
from .helper import email_auth_num, send_mail
from .models import User
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template   
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View


from .decorators import *
import requests
import json



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationform(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            return redirect('/')
    else:
        form = CustomUserCreationform()
    return render(request, 'signup.html', {
        'form':form
})

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error': 'username or password is incorrect.'})
    else: 
        return render(request,'login.html')

def logout(request):
    # if request.method =="POST":
    auth.logout(request)
    return redirect('home')
    # return render(request, 'login.html')

def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST,instance = request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('/')
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)    
        return render(request, 'update.html',{'user_change_form':user_change_form})


@method_decorator(logout_message_required, name='dispatch')
class RecoveryPwView(View):
    template_name = 'recovery_pw.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_pw(None)
            return render(request, self.template_name, { 'form':form, })

def ajax_find_pw_view(request):
    username = request.POST.get('username')
    name = request.POST.get('name')
    email = request.POST.get('email')
    target_user = User.objects.get(username=username, name=name, email=email)
    print("타겟 유저", username, name, email)

    if target_user:
        auth_num = email_auth_num()
        target_user.auth = auth_num 
        target_user.save()

        send_mail(
            '비밀번호 찾기 인증메일입니다.',
            [email],
            html=render_to_string('recovery_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")

# 인증번호 확인
def auth_confirm_view(request):
    username = request.POST.get('username')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = User.objects.get(username=username, auth=input_auth_num)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.username  
    print("타겟 유저", target_user)
    print("인증번호",input_auth_num)
    
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")


@logout_message_required
def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(user_id=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)
        
        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'password_reset.html', {'form':reset_password_form})