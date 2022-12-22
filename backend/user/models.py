from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from base.models import Subject, Standard, Department
import uuid

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
        return self._create_user(email, password, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

CUSTOMUSER_POSITION_CHOICES = (
    ('Staff', 'Staff'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Admin', 'Admin'),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    position = models.CharField(choices=CUSTOMUSER_POSITION_CHOICES, max_length=100, default="Staff")
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

GENDER_CHOICES = (
    ("M", "M"),
    ("F", "F"),
    ("O", "O"),
)

class Teacher(models.Model):

    teacherId = models.UUIDField(default = uuid.uuid4, unique=True)
    teacherName = models.CharField(max_length=1000, default="Guest Teacher")
    teacherSubject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    teacherUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    teacherImage = models.ImageField(upload_to='teacherimage/', default="default.png")
    teacherJoiningDate = models.DateField(auto_now_add=True)
    teacherPayScale = models.IntegerField(default=0)
    teacherBio = models.TextField(default="Bio")
    teacherGender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    teacherMobileNumber = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Student(models.Model):

    studentUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    studentId = models.UUIDField(default = uuid.uuid4, unique=True)
    studentName = models.CharField(max_length=1000, default="Guest Student")
    studentClass = models.ForeignKey(Standard, on_delete=models.SET_DEFAULT, default="undefined")
    studentSubject = models.ManyToManyField(Subject, blank=True)
    studentImage = models.ImageField(upload_to='studentimage/', default="default.png")
    studentJoiningDate = models.DateField(auto_now_add=True)
    studentBio = models.TextField(default="Bio")
    studentGender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    studentMobileNumber = models.CharField(max_length=100, default="")
    studentMarks = models.IntegerField(default=0)
    studentRemarks = models.TextField(default="Remarks")
    studentRating = models.CharField(max_length=1, choices=RATING_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Staff(models.Model):

    staffUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    staffId = models.UUIDField(default = uuid.uuid4, unique=True)
    staffName = models.CharField(max_length=1000, default="Guest Staff")
    staffDepartment = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    staffPayScale = models.IntegerField(default=0)
    staffImage = models.ImageField(upload_to='staffimage/', default="default.png")
    staffJoiningDate = models.DateField(auto_now_add=True)
    staffBio = models.TextField(default="Bio")
    staffGender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    staffMobileNumber = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
