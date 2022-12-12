from django.db import models

# Create your models here.

class Subject(models.Model):

    subjectName = models.CharField(max_length=1000, primary_key=True, unique=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'