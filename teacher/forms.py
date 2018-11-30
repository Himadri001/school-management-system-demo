from django import forms
from .models import Teachers

class AddTeacherForm(forms.ModelForm):
     gender_option =(
                    ("Male", "Male"),
                    ("Female", "Female"),
                    )
     teacher_name = forms.CharField(widget=forms.TextInput())
     phone_number = forms.CharField(widget=forms.TextInput())
     address = forms.CharField(widget=forms.TextInput())
     gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              choices=gender_option)

     class Meta:
        model = Teachers
        fields = ('teacher_name', 'phone_number', 'gender', 'address',)
