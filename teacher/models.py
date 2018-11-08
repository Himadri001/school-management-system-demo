from django.db import models
from django.contrib.auth.models import AbstractUser

# Teacher model attribute
class Teacher(models.Model):
    # auto updating id
    id = models.AutoField(primary_key=True)
    #gender_choices = [('M', 'Male'), ('F', 'Female')]
    teacher_name = models.TextField(max_length=200, null=True)
    phone_number = models.TextField(max_length=200, null=True)

    def __str__(self):
        return str(self.teacher_name)
