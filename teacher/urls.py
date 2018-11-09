# urls.py
from django.urls import path
from teacher.views import Teacher

urlpatterns = [
    path('addteacher/', Teacher.as_view()),
]
