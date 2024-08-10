"""Import the specified module"""
from django.contrib import admin
from django.urls import include, path
from todos.views import HomeView, CreatePage, UpdatePage, DeleteTodo, MarkDoneTodo, DoneTodo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('create-todo/', CreatePage.as_view(), name='create'),
    path('done/', DoneTodo.as_view(), name='done'),
    path('mark-done/<int:pk>/', MarkDoneTodo.as_view(), name='mark_todo_done'), 
    path('edit-todo/<int:pk>/', UpdatePage.as_view(), name='edit_todo'), 
    path('delete-todo/<int:pk>/', DeleteTodo.as_view(), name='delete_todo'),
    path('auth/',include('authentication.urls')),
    path('regis/', include('registration.urls')),
]
