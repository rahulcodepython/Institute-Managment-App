from django.contrib import admin
from authentication.models import CustomUser, Teacher, Student, Staff, UnapprovedUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'position']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacherUser', 'teacherSubject']

@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['studentUser', 'studentClass']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staffUser', 'staffDepartment']

@admin.register(UnapprovedUser)
class UnapprovedUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'position', 'name']

