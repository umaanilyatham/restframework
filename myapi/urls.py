from django.contrib import admin
from django.urls import path
from .views import EmployeeAPIView

urlpatterns = [
    path('employees/', EmployeeAPIView.as_view()),
    path('employees/<int:pk>/', EmployeeAPIView.as_view()),
]
