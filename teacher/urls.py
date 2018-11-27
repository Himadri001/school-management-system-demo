# urls.py
from django.urls import path
from teacher.views import TeacherView

urlpatterns = [
    path('addteacher/', TeacherView.as_view(), name='teacher'),
    path('viewteacher/', TeacherView.as_view(template_name= 'view_teacher.html'), name='teacher'),
]
