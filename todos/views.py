from django.shortcuts import render
from .models import *
def todo_list(request):
    todos = Todos.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})
def mark_todo_done(request):
    todo_id = request.POST.get('todo_id')
    todo = Todos.objects.get(id=todo_id)
    todo.is_done = True
    todo.save()
    return render(request, 'todos/todo_list.html')