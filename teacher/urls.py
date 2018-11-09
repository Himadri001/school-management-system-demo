# urls.py
from django.urls import path
from teacher import views

urlpatterns = [
    path('addteacher/', views.teacher, name='teacher'),
]
