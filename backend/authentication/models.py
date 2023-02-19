from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from base.models import Standard, Domain, Subdomain, Department

GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
]
POSITION = [
    ('Staff', 'Staff'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student')
]

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

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    joiningDate = models.DateField(auto_now_add=True)

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='userimage/', default="default.png")
    aboutme = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER)
    mobile = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITION)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

# Base Employee
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    salary = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    class Meta:
        managed = False

# Teacher Model
class Teacher(Employee):
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    subdomain = models.ForeignKey(Subdomain, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

# Staff Model
class Staff(Employee):
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'

# Student Model
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True, blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True, blank=True)
    subdomain = models.ManyToManyField(Subdomain, blank=True)
    is_session_active = models.BooleanField(default=False)
    is_fees_clear = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
