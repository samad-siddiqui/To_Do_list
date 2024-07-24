from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def signUp(request):
    if request.method == "POST":
        usname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conpassword = request.POST.get('conpassword')
        if password != conpassword:
            return HttpResponse("Passwords do not match")
        else:
            user = User.objects.create_user(usname,email,password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')
