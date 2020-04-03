from django.shortcuts import render
from .forms import CustomUserCreationform
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
    if request.method =="POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')