# urls.py
from django.urls import path
from teacher.views import TeacherView

urlpatterns = [
    path('addteacher/', TeacherView.as_view(), name='teacher'),
    #path('addteacher/')
]
