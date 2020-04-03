from django.shortcuts import render
from .forms import CustomUserCreationform, CustomUserChangeForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib import auth

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
            return redirect('home',request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)    
        return render(request, 'update.html',{'user_change_form':user_change_form})
