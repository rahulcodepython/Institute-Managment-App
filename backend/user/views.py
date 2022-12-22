from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import Teacher, Student, CustomUser, Staff
from user.serializers import (
    RegisterUserToCustomUserModelSerializer, 
    ProfileButtonTeacherSerializer, 
    ProfileButtonStaffSerializer, 
    ProfileButtonStudentSerializer, 
    ShowTeachersSerializer, 
    ShowStudentsSerializer,
    ShowProfileTeacherPrivateSerializer,
    ShowProfileStaffPrivateSerializer,
    ShowProfileStudentPrivateSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Show Profile button
class ProfileButtonView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        position = CustomUser.objects.get(email=self.request.user).position
        if position == 'Teacher':
            return Teacher.objects.filter(teacherUser=self.request.user)
        elif position == 'Student':
            return Student.objects.filter(studentUser=self.request.user)
        elif position == 'Staff' or position == 'Admin':
            return Staff.objects.filter(staffUser=self.request.user)

    def get_serializer_class(self):
        position = CustomUser.objects.get(email=self.request.user).position
        if position == 'Teacher':
            return ProfileButtonTeacherSerializer
        elif position == 'Student':
            return ProfileButtonStudentSerializer
        elif position == 'Staff' or position == 'Admin':
            return ProfileButtonStaffSerializer

# Show Teachers for Admin
class ShowTeachersView(generics.ListAPIView):

    serializer_class = ShowTeachersSerializer
    queryset = Teacher.objects.all()
    permission_classes = [IsAdminUser]

# Show Students for Admin
class ShowStudentsView(generics.ListAPIView):

    serializer_class = ShowStudentsSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAdminUser]

# Register New User
class RegisterUserToCustomUserModelView(generics.CreateAPIView):
    serializer_class = RegisterUserToCustomUserModelSerializer
    queryset = CustomUser

# Show Profile
class ShowProfilePrivateView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        position = CustomUser.objects.get(email=self.request.user).position

        if position == 'Teacher':
            return Teacher.objects.filter(teacherUser=self.request.user)
        elif position == 'Student':
            return Student.objects.filter(studentUser=self.request.user)
        elif position == 'Staff' or position == 'Admin':
            return Staff.objects.filter(staffUser=self.request.user)

    def get_serializer_class(self):
        position = CustomUser.objects.get(email=self.request.user).position

        if position == 'Teacher':
            return ShowProfileTeacherPrivateSerializer
        elif position == 'Student':
            return ShowProfileStudentPrivateSerializer
        elif position == 'Staff' or position == 'Admin':
            return ShowProfileStaffPrivateSerializer


