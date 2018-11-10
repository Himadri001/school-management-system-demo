from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import AddTeacherForm

# Create your views here.
class TeacherView(TemplateView):
     template_name = "add_teacher.html"
     def get(self,request):
         return render(request,'add_teacher.html')
     def post(self, request):
         form = AddTeacherForm(request.POST)
         if form.is_valid():
            template_name = "page2.html"
            teacher = form.save(commit=False)
            teacher.save()
            teacher_name = form.cleaned_data['teacher_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            return render(request, 'page2.html',{})
         else:
             form = AddTeacherForm()
         return render(request,'add_teacher.html')
