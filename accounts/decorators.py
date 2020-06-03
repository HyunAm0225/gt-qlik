from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse

# 로그인 확인
def login_message_required(function):
    def wrap(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.info(request,"로그인한 사용자만 이용할 수 있습니다.")
            # 수정 해야함 
            return redirect(settings.LOGIN_URL)
        return function(request,*args,**kwargs)
    return wrap

# 관리자 권한 확인
def admin_required(function):
    def wrap(request,*args,**kwargs):
        if request.user.name == '관리자' or request.user.rank == '개발자':
            return function(request,*args,**kwargs)
        messages.info(request,"접근 권한이 없습니다.")
        # 수정 해야함
        return redirect('/')
    return wrap

# 비로그인 확인
def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            # 수정 해야함
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrap
