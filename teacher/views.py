from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from teacher.forms import AddTeacherForm
from teacher.models import Teachers

# Create your views here.
class TeacherView(TemplateView):
     template_name = 'add_teacher.html'
     def teacher_dashboard(self, request):
         teacher_results = Teachers.object.all()
         print(teacher_results)
         return render(request, 'view_teacher.html', teacher_results)
     def get(self,request):
         return render(request,'add_teacher.html')
     def post(self, request):
         form = AddTeacherForm(request.POST)
         if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            teacher_name = form.cleaned_data['teacher_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            return render(request, 'add_teacher.html', {})
         else:
             form = AddTeacherForm()
         return render(request,'add_teacher.html')
