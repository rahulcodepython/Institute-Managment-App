from django.contrib import admin
from base.models import Log, Standard, Department, Domain, Subdomain

# # Register your models here.

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    model = Log
    list_display = ['createdAt', 'log']

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ['standard']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Subdomain)
class SubdomainAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dept']