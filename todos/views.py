from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todos.models import Todo

@login_required(login_url='login')
def home(request):
    query = request.GET.get('q', '')
    if query:
        todos = Todo.objects.filter(title__icontains=query) | Todo.objects.filter(description__icontains=query)
    else:
        todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})
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

    