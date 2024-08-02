from todos import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('crt/', views.createpage, name='create'),
    path('done/', views.done_todo, name='done'),
    path('mark-done/<int:todo_id>/', views.mark_todo_done, name='mark_todo_done'), 
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'), 
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('auth/',include('authentication.urls')),
    path('regis/', include('registration.urls')),
]
