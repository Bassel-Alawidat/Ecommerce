from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .forms import RegiserForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegiserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}')
            return redirect('users:login')
    else:
        form = RegiserForm()
    return render(request, 'users/register.html', {'form': form})
 
# def login(request):
#     context={}
#     return render(request,'users/login.html',context)
# def logout(request):
#     context={}
#     return render(request,'users/logout.html',context)

def profilepage(request):
    return render(request,'users/profile.html')





