from django.urls import path
from create_todo import views

urlpatterns = [
    path('create/', views.createpage, name='create'),
]