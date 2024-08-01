"""import shortcuts"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from todos.models import Todo
from .forms import TodoForm

@login_required(login_url='login')
def home(request):
    '''Home page for logged in users.'''
    query = request.GET.get('q', '')
    if query:
        todos = Todo.objects.filter(user=request.user).filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})
@login_required(login_url='login')
def mark_todo_done(request,todo_id):
    '''Mark todo as done.'''
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.is_done = True
            todo.save()
            return redirect('home')
        else:
            return redirect('home')
@login_required(login_url='login')
def edit_todo(request, todo_id):
    '''Edits a todo.'''
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit.html', {'form': form})
@login_required(login_url='login')
def delete_todo(request, todo_id):
    '''Delete todo.'''
    todo = Todo.objects.get(id=todo_id, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('home')
    return render(request, 'delete.html', {'todo': todo})
@login_required(login_url='login')
def done_todo(request):
     '''Shows done todos.'''
     done_todos = Todo.objects.filter(user=request.user, is_done=True)
     return render(request, 'done.html', {'todos': done_todos})
 