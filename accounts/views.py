from django.shortcuts import render
from .forms import CustomUserCreationform

# Create your views here.
def signup(request):
    form = CustomUserCreationform()
    return render(request, 'signup.html',{'form':form})

def login(request):
    return render(request,'login.html')