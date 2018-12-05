from django import forms
from .models import Teachers

class AddTeacherForm(forms.ModelForm):

     class Meta:
        model = Teachers
        fields = ['teacher_name', 'phone_number', 'gender', 'address',]
