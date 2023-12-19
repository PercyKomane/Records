from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('newEmployee/', views.newEmployee, name='newEmployee'),
    path('employeeDetails/<str:pk>/', views.employeeDetails, name='employeeDetails'),
    path('delete/<str:pk>/', views.deleteRecord, name='delete'),
]