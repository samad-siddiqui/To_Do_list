from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from todos.models import Todo

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
  

def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todo(user=request.user, title=title, description=description)
        todo.save()
        return redirect('home')
    return render(request, 'create.html')

def mark_todo_done(todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_done = True
    todo.save()
    return redirect('home')

def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('home')
    return render(request, 'edit.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.delete()
        return redirect('home')
    return render(request, 'delete.html', {'todo': todo})

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