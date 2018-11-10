from django import forms
from .models import Teachers

class AddTeacherForm(forms.ModelForm):
     teacher_name = forms.CharField(widget=forms.TextInput())
     phone_number = forms.CharField(widget=forms.TextInput())
     address = forms.CharField(widget=forms.TextInput())

     class Meta:
        model = Teachers
        fields = ('teacher_name', 'phone_number', 'address',)
