from django.contrib import admin
from base.models import Subject, Standard, Department

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectName']

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ['className']

@admin.register(Department)
class DepartmentdAdmin(admin.ModelAdmin):
    list_display = ['departmentName']
