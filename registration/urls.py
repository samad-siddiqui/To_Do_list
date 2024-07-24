 
from django.urls import path
from registration import views
 
urlpatterns = [
    path('register/', views.signUp, name='register'),
    ]