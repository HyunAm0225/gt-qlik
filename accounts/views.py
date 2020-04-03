from django.shortcuts import render
from .forms import CustomUserCreationform
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect

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
    return render(request,'login.html')