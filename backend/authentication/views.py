from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import UnapprovedUser, CustomUser, Staff, Student, Teacher
from .serializers import TeacherSerializer, StaffSerializer, StudentSerializer, UnapprovedUserSerializer, CustomUserSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    def post(self, request, format=None):
        if UnapprovedUser.objects.filter(email=request.data['email']).exists() or CustomUser.objects.filter(email=request.data['email']).exists():
            return Response({"error": "You exists already."})
        else:
            serialized = UnapprovedUserSerializer(data=request.data)

            if serialized.is_valid():
                serialized.save()
                return Response({"msg": "You have registered. Please wait for furthur action from admin."})

            else:
                return Response({"error": "There is some issue. Please try again."})

class AddUserView(APIView):

    def post(self, request, formate=None):
        if request.user.is_superuser:
            email = request.data['email']
            if UnapprovedUser.objects.filter(email=email).exists():
                user = UnapprovedUser.objects.get(email=email)
                newUser = CustomUser(email=user.email, name=user.name, password=user.password, position=user.position)
                newUser.save()
                user.delete()

                if user.position == 'Staff' or user.position == 'Admin':
                    Staff(staffUser=newUser).save()
                elif user.position == 'Teacher':
                    Teacher(teacherUser=newUser).save()
                elif user.position == 'Student':
                    Student(studentUser=newUser).save()

                return Response({"msg": "New user is created."})
            else:
                return Response({"error": "There exists no such user."})
        else:
            return Response({"error": "You are not admin."})

class DeleteUnapprovedUserView(APIView):

    def delete(self, request, format=None):
        if request.user.is_superuser:
            if UnapprovedUser.objects.filter(email=request.data['email']).exists():
                UnapprovedUser.objects.get(email=request.data['email']).delete()
                return Response({"msg": "The user is deleted."})
            else:
                return Response({"error": "This user does not exists."})
        else:
            return Response({"error": "You are not admin."})

class LoginView(APIView):
    def post(self, request, format=None):
        user = authenticate(email=request.data['email'], password=request.data['password'])
        
        if user is not None:
            token = get_tokens_for_user(user)
            if user.position == 'Teacher':
                image = Teacher.objects.get(teacherUser=user).teacherImage
            elif user.position == 'Student':
                image = Student.objects.get(studentUser=user).studentImage
            elif user.position == 'Staff' or user.position == 'Admin':
                image = Staff.objects.get(staffUser=user).staffImage

            return Response({
                'token' : token,
                'user': {
                    'name': user.name,
                    'email': user.email,
                    'image': image.url,
                    'position': user.position
                }
            })
        else:
            return Response({"error": "User is none"})

class DeleteUserView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        if request.user.position == 'Admin':
            user = CustomUser.objects.get(email=request.data['email'])
        
        else:
            user = CustomUser.objects.get(email=request.user)

        user.delete()
        return Response({"msg": "The user is deleted."})

class ShowSelfView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if request.user.position == 'Admin':
            user = CustomUser.objects.get(email=request.data['email'])
        
        else:
            user = CustomUser.objects.get(email=request.user.email)

        if user.position == 'Teacher':
            teacher = Teacher.objects.get(teacherUser=user)
            serialized_data = TeacherSerializer(teacher)

        elif user.position == 'Student':
            student = Student.objects.get(studentUser=user)
            serialized_data = StudentSerializer(student)

        elif user.position == 'Staff' or user.position == 'Admin':
            staff = Staff.objects.get(staffUser=user)
            serialized_data = StaffSerializer(staff)
        
        return Response({
            'data': serialized_data.data,
            'user' : {
                'name': user.name,
                'email': user.email,
                'joiningDate': user.joiningDate
            }
            })

class ShowAllTeachersView(APIView):

    def get(self, request, format=None):
        if request.user.is_superuser:
            return Response(TeacherSerializer(Teacher.objects.all(), many=True).data)
        else:
            return Response({"error": "You are not admin."})

class ShowAllStudentsView(APIView):

    def get(self, request, format=None):
        if request.user.is_superuser:
            return Response(StudentSerializer(Student.objects.all(), many=True).data)
        else:
            return Response({"error": "You are not admin."})

class ShowAllStaffsView(APIView):

    def get(self, request, format=None):
        if request.user.is_superuser:
            return Response(StaffSerializer(Staff.objects.all(), many=True).data)
        else:
            return Response({"error": "You are not admin."})

class SelfUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, format=None):
        user = CustomUser.objects.get(email=request.user.email)

        if user.position == 'Teacher':
            teacher = Teacher.objects.get(teacherUser=user)
            serializer = TeacherSerializer(teacher, data=request.data, partial=True)

        elif user.position == 'Student':
            student = Student.objects.get(studentUser=request.user)
            serializer = StudentSerializer(student, data=request.data, partial=True)

        elif user.position == 'Staff' or user.position == 'Admin':
            staff = Staff.objects.get(staffUser=request.user)
            serializer = StaffSerializer(staff, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            
            return Response({"msg": "Your data is updated."})
        
        else:
            return Response({"error": "There is some issue."})

class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(seld, request, format=None):
        user = CustomUser.objects.get(email=request.user.email)

        serialized = CustomUserSerializer(user, data=request.data, partial=True)

        if serialized.is_valid():
            serialized.save()

            return Response({"msg": "Your password is updated."})
    
        return Response({"error": "There is some issue."})

        

