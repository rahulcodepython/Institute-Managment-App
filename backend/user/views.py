from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import Teacher, Student, CustomUser, Staff, WaitingApproval
from user.serializers import (
    RegisterUserToCustomUserModelSerializer, 
    ProfileButtonTeacherSerializer, 
    ProfileButtonStaffSerializer, 
    ProfileButtonStudentSerializer, 
    ShowTeachersSerializer, 
    ShowStudentsSerializer,
    ShowProfileTeacherPrivateSerializer,
    ShowProfileStaffPrivateSerializer,
    ShowProfileStudentPrivateSerializer,
    WaitForApprovalRegisterUserToCustomUserModelSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView, Response

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Show Profile button
class ProfileButtonView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        position = CustomUser.objects.get(email=self.request.user).position

        if position == 'Teacher':
            teacher = Teacher.objects.get(teacherUser=self.request.user)
            serialized = ProfileButtonTeacherSerializer(teacher)

            return Response(serialized.data)

        elif position == 'Student':
            student = Student.objects.get(studentUser=self.request.user)
            serialized = ProfileButtonStudentSerializer(student)

            return Response(serialized.data)

        elif position == 'Admin' or position == 'Staff':
            staff = Staff.objects.get(staffUser=self.request.user)
            serialized = ProfileButtonStaffSerializer(staff)

            return Response(serialized.data)

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

# Wait New User For Approval From Admin
class WaitForApprovalRegisterUserToCustomUserModelView(generics.CreateAPIView):
    serializer_class = WaitForApprovalRegisterUserToCustomUserModelSerializer
    queryset = WaitingApproval

# Check Waiting User is till not approved
class CheckWaitForApprovalRegisterUserToCustomUserModelView(APIView):
    
    def get(self, request, id, format=None): 
        if WaitingApproval.objects.filter(name=id).exists():
            return Response({"msg": "Not Approved"})
        
        elif CustomUser.objects.filter(name=id).exists():
            return Response({"msg": "Approved"})

        else:
            return Response({"msg": "Rejected"})
            
# Show Profile
class ShowProfilePrivateView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, id, format=None):
        requestUserPosition = CustomUser.objects.get(email=request.user.email).position
        user = CustomUser.objects.get(name=id)
        userposition = CustomUser.objects.get(name=id).position

        if requestUserPosition == 'Admin' and userposition == 'Teacher':
            teacher = Teacher.objects.get(teacherUser=user)
            serialized = ShowProfileTeacherPrivateSerializer(teacher)
            print("teacher")

        elif requestUserPosition == 'Admin' and userposition == 'Student':
            student = Student.objects.get(studentUser=user)
            serialized = ShowProfileStudentPrivateSerializer(student)

        elif requestUserPosition == 'Admin' and userposition == 'Staff' or userposition == 'Admin':
            staff = Staff.objects.get(staffUser=user)
            serialized = ShowProfileStaffPrivateSerializer(staff)
        
        return Response(serialized.data)
    


