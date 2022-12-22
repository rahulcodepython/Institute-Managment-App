from django.db import models

# Create your models here.

class Subject(models.Model):

    subjectName = models.CharField(max_length=1000, primary_key=True, unique=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Standard(models.Model):

    className = models.CharField(max_length=1000, primary_key=True, unique=True)

    class Meta:
        verbose_name = 'Standard'
        verbose_name_plural = 'Standards'

class Department(models.Model):
    
    departmentName = models.CharField(max_length=100, primary_key=True, unique=True)

