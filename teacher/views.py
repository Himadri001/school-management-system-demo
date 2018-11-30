from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from teacher.forms import AddTeacherForm
from teacher.models import Teachers
from teacher.models import Teachers

# Create your views here.
class TeacherAddView(TemplateView):
     # get method for showing the page
     def get(self,request):
         return render(request,'add_teacher.html',{})


     def post(self, request):
         form = AddTeacherForm(request.POST)
         if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            teacher_name = form.cleaned_data['teacher_name']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            return render(request, 'add_teacher.html', {})
         else:
             form = AddTeacherForm()

# teacher dashboard create
class TeacherDashboardView(TemplateView):

    def get(self, request):
        models = Teachers
        teacher_results = Teachers.objects.all()
        print(teacher_results)
        return render(request, 'view_teacher.html', {'teacher_results': teacher_results})
