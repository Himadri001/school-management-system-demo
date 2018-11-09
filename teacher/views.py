from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Teacher(TemplateView):
     template_name = "add_teacher.html"
