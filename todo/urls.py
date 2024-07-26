from todos import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create_todo'), 
    path('edit/', views.edit_todo, name='edit_todo'), 
    path('auth/',include('authentication.urls')),
    path('regis/', include('registration.urls')),
]
