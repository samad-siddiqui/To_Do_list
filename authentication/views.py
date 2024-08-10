from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import  LoginForm

# # Create your views here.
def loginpage(request):
    """user login page"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def logoutpage(request):
    """user logout"""
    logout(request)
    return redirect('login')