# urls.py
from django.urls import path
from teacher.views import TeacherAddView, TeacherDashboardView

urlpatterns = [
    path('addteacher/', TeacherAddView.as_view(), name='teacher'),
    path('viewteacher/', TeacherDashboardView.as_view(), name='teacher'),
]
