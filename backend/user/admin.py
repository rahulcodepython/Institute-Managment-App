from django.contrib import admin
from user.models import CustomUser, Teacher, Student, Staff, WaitingApproval

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacherName', 'teacherUser', 'teacherSubject']

@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['studentName', 'studentUser', 'studentClass']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staffName', 'staffUser', 'staffDepartment']

@admin.register(WaitingApproval)
class WaitingApprovalAdmin(admin.ModelAdmin):
    list_display = ['email', 'position']

