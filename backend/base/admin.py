from django.contrib import admin
from base.models import Subject

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectName']
