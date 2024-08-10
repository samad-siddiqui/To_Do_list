"""import shortcuts"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q
from todos.models import Todo
from .forms import TodoForm
@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(ListView):
    '''Home page for logged in users.'''
    model = Todo
    template_name = 'home.html'
    context_object_name = 'todos'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Todo.objects.filter(user=self.request.user).filter(Q(title__icontains=query) | Q(description__icontains=query))
        else:
            return Todo.objects.filter(user=self.request.user)
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreatePage(CreateView):
    '''Create a new todo'''
    model = Todo
    template_name = 'create.html'
    form_class = TodoForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdatePage(UpdateView):
    '''Update an existing todo'''
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'todos'
    form_class = TodoForm
    success_url = reverse_lazy('home')
    def get_object(self):
        return Todo.objects.get(id=self.kwargs['pk'], user=self.request.user)
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteTodo(DeleteView):
    '''Delete a todo'''
    model = Todo
    template_name = 'delete.html'
    context_object_name = "todos"
    success_url = reverse_lazy('home')
    def get_object(self, **kwargs):
        return Todo.objects.get(id=self.kwargs['pk'], user=self.request.user)
@method_decorator(login_required(login_url='login'), name='dispatch')
class MarkDoneTodo(UpdateView):
    '''Mark todo as done.'''
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('home')
    def form_valid(self):
        todo = self.get_object()
        todo.is_done = True
        todo.save()
        return redirect(self.success_url)
@method_decorator(login_required(login_url='login'), name='dispatch')
class DoneTodo(ListView):
    '''Shows done todos.'''
    model = Todo
    template_name = 'done.html'
    context_object_name = 'todos'
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user, is_done=True)
# 
# # @login_required(login_url='login')
# def home(request):
#     '''Home page for logged in users.'''
#     query = request.GET.get('q', '')
#     if query:
#         todos = Todo.objects.filter(user=request.user).filter(Q(title__icontains=query) | Q(description__icontains=query))
#     else:
#         todos = Todo.objects.all()
#     return render(request, 'home.html', {'todos': todos})
# def createpage(request):
#     """Create a new todo"""
#     if request.method == "POST":
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             title = request.POST.get('title')
#             description = request.POST.get('description')
#             todo = Todo(user=request.user, title=title, description=description)
#             todo.save()
#         return redirect('home')
#     else:
#         form = TodoForm()
#         return render(request, 'create.html', {'form': form})
# @login_required(login_url='login')
# def edit_todo(request, todo_id):
#     '''Edits a todo.'''
#     todo = get_object_or_404(Todo, id=todo_id, user=request.user)
#     if request.method == "POST":
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'edit.html', {'form': form})
# @login_required(login_url='login')
# def delete_todo(request, todo_id):
#     '''Delete todo.'''
#     todo = Todo.objects.get(id=todo_id, user=request.user)
#     if request.method == "POST":
#         todo.delete()
#         return redirect('home')
#     return render(request, 'delete.html', {'todo': todo})
#@login_required(login_url='login')
# def mark_todo_done(request,todo_id):
#     '''Mark todo as done.'''
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             todo = Todo.objects.get(id=todo_id, user=request.user)
#             todo.is_done = True
#             todo.save()
#             return redirect('home')
#         else:
#             return redirect('home')
# @login_required(login_url='login')
# def done_todo(request):
#      '''Shows done todos.'''
#      done_todos = Todo.objects.filter(user=request.user, is_done=True)
#      return render(request, 'done.html', {'todos': done_todos})
