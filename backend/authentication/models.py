from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

# Custom Base User
class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=255, default="")
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    position = models.CharField(max_length=100, default="Staff")
    joiningDate = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

# Teacher Model
class Teacher(models.Model):

    teacherUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    teacherSubject = models.CharField(max_length=100, default="", blank=True)
    teacherImage = models.ImageField(upload_to='teacherimage/', default="default.png")
    teacherLastUpdateDate = models.DateField(auto_now=True)
    teacherPayScale = models.IntegerField(default=0)
    teacherBio = models.TextField(default="Bio")
    teacherGender = models.CharField(max_length=1, default="")
    teacherMobileNumber = models.CharField(max_length=100, default="", blank=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

# Student Model
class Student(models.Model):

    studentUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    studentClass = models.CharField(max_length=100, default="", blank=True)
    studentSubject = models.CharField(max_length=100, default="", blank=True)
    studentImage = models.ImageField(upload_to='studentimage/', default="default.png")
    studentLastUpdateDate = models.DateField(auto_now=True)
    studentBio = models.TextField(default="Bio")
    studentGender = models.CharField(max_length=1, default="", blank=True)
    studentMobileNumber = models.CharField(max_length=100, default="", blank=True)
    studentMarks = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

# Staff Model
class Staff(models.Model):

    staffUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    staffDepartment = models.CharField(max_length=100, default="", blank=True)
    staffPayScale = models.IntegerField(default=0)
    staffImage = models.ImageField(upload_to='staffimage/', default="default.png")
    staffLastUpdateDate = models.DateField(auto_now=True)
    staffBio = models.TextField(default="Bio")
    staffGender = models.CharField(max_length=1, default="", blank=True)
    staffMobileNumber = models.CharField(max_length=100, default="", blank=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'

# Unapproved User Model
class UnapprovedUser(models.Model):

    email = models.EmailField(unique=True, max_length=254)
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    position = models.CharField(max_length=100, default="Staff")
    joiningDate = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

