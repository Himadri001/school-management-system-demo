# urls.py
from django.urls import path
from teacher.views import TeacherAddView, TeacherDashboardView

urlpatterns = [
    path('addteacher/', TeacherAddView.as_view(template_name='add_teacher.html'), name='teacher'),
    path('viewteacher/', TeacherDashboardView.as_view(template_name='view_teacher.html'), name='teacher'),
]
