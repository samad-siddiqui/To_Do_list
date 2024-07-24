from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")
    
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')