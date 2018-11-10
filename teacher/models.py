from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


# Teacher model create
class Teachers(models.Model):
    # Field name
    teacher_name = models.TextField(max_length=200, null=True)
    phone_number = models.TextField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.teacher_name)

        super(Teachers, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.teacher_name)
    # Metadata
    class Meta:
        #
        ordering = ['teacher_name']
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
