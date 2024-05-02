from django.urls import path
from api import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('create_budget/', views.create_budget, name='create_budget'),
    path('create_expense/', views.create_expense, name='create_expense'),
]