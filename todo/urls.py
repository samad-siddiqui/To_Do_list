from django.urls import path
from todos import views

# urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('register/', views.signUp, name='register'),
#     path('login/', views.loginPage, name='login'),
#     path('logout/', views.logoutPage, name='logout'),
#     path('create/', views.create_todo),
#     path('edit/<int:todo_id>/', views.edit_todo),
#     path('delete/<int:todo_id>/', views.delete_todo),
# ]
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create_todo'),  # Update to match the pattern you want
    path('edit/', views.edit_todo, name='edit_todo'),  # Update to match the pattern you want
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),  # Update to match the pattern you want
    path('register/', views.signUp, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),  # Ensure you have a logout view if using this URL
]
