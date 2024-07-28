from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from todos.models import Todo

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html',{'todos': Todo.objects.all()})
  
@login_required(login_url='login')
def mark_todo_done(request,todo_id):
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


