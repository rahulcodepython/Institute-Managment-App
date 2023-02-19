from django.db import models

# Create your models here.

class Log(models.Model):
    log = models.CharField(max_length=1000, primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

class Standard(models.Model):
    standard = models.CharField(max_length=100, primary_key=True, unique=True)

class Domain(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)

class Subdomain(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

class Department(models.Model):
    dept = models.CharField(max_length=100, primary_key=True, unique=True)