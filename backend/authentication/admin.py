from django.contrib import admin
# from authentication.models import CustomUser
from authentication.models import CustomUser, Teacher, Student, Staff

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'position']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'domain', 'subdomain']

@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'standard', 'domain']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'dept']

