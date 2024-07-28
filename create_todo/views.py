from django.shortcuts import render,redirect
from .forms import CreateForm
from todos.models import Todo

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def createpage(request):
    """Create a new todo"""
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            todo = Todo(user=request.user, title=title, description=description)
        todo.save()
        return redirect('home')
    return render(request, 'create.html')