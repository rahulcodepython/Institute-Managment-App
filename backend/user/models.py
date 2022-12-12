from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from base.models import Subject
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

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    
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

    teacherId = models.UUIDField(primary_key = True, default = uuid.uuid4, unique=True)
    teacherName = models.CharField(max_length=1000, default="Guest Teacher")
    teacherSubject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    teacherUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacherImage = models.ImageField(upload_to='teacherimage/')
    teacherJoiningDate = models.DateField(auto_now_add=True)
    teacherBio = models.TextField()
    teacherGender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    teacherMobileNumber = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'