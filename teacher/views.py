from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def teacher(request):
    if (request.method=="POST"):
        print('okay')
    if (request.method=="GET"):
        return render(request, 'add_teacher.html')
#class Teacher(TemplateView):
     #template_name = "add_teacher.html"
