from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer, StaffSerializer, TeacherSerializer, StudentSerializer
from base.models import Log

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': f'{refresh}',
        'access': f'{refresh.access_token}',
    }

class RegisterView(APIView):

    def post(self, request, format=None):
        try:
            if 'email' in request.data and CustomUser.objects.filter(email=request.data['email']).exists():
                return Response({"error": "This user already exists."})

            serialized_user = CustomUserSerializer(data=request.data)

            if not serialized_user.is_valid():
                return Response({"error": "Given data is not valid." })

            if request.data['position'] == 'Teacher':
                if 'domain' not in request.data or 'subdomain' not in request.data:
                    return Response({"error": "Required data is not fulfiled. Please try again." })

                serialized = TeacherSerializer(data=request.data)

            elif request.data['position'] == 'Staff':
                if 'dept' not in request.data:
                    return Response({"error": "Required data is not fulfiled. Please try again." })

                serialized = StaffSerializer(data=request.data)
                
            elif request.data['position'] == 'Student':
                if 'standard' not in request.data or 'domain' not in request.data:
                    return Response({"error": "Required data is not fulfiled. Please try again."})

                serialized = StudentSerializer(data=request.data)   

            if not serialized.is_valid():
                return Response({"error": "Given data is not valid."})

            serialized_user.save()
            serialized.save(user=CustomUser.objects.get(email=request.data['email']))  

            Log(log=f"{request.data['email']} is created.").save()

            return Response({"msg": "New user is created."})

        except Exception as e:
            return Response(e)

class LoginView(APIView):

    def post(self, request, format=None):
        try:
            if "email" not in request.data or "password" not in request.data:
                return Response({"error": "Required data is not fulfiled. Please try again."})
                
            user = authenticate(email=request.data['email'], password=request.data['password'])
            
            if user is None:
                return Response({"error": "No such user exists."})

            return Response({
                'token': get_tokens_for_user(user),
                'user': {
                    'name': user.name,
                    'email': user.email,
                    'image': user.image.url
                }
            })
    
        except Exception as e:
            return Response(e)

class AddUserView(APIView):

    def post(self, request, formate=None):
        try:
            if not request.user.is_superuser:
                return Response({"error": "You are not admin to process it."})

            if "email" not in request.data:
                return Response({"error": "Required data is not fulfiled. Please try again."})
                
            if not CustomUser.objects.filter(email=request.data['email']).exists():
                return Response({"error": "No such user exists."})
                
            if CustomUser.objects.get(email=request.data['email']).is_active:
                return Response({"error": "The user is already approved."})

            user = CustomUser.objects.get(email=request.data['email'])
            user.is_active = True
            user.save()
            
            Log(log=f"{request.user} has approved {user.email} user").save()

            return Response({"msg": "New user is registerd."})

        except Exception as e:
            return Response(e)

class SelfUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, format=None):
        try:
            if 'position' in request.data or 'password' in request.data:
                return Response({"error": "You can not update your position and password from here."})

            user = CustomUser.objects.get(email=request.user.email)

            serializer = CustomUserSerializer(user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                Log(log=f"{request.user.email} has updated own profile").save()

                return Response({"msg": "Your data is updated."})
            
            return Response({"error": "There is some issue. Please try again."})
            
        except Exception as e:
            return Response(e)

class UpdatePasswordView(APIView):

    permission_classes = [IsAuthenticated]

    def post(seld, request, format=None):
        try:
            user = CustomUser.objects.get(email=request.user.email)

            if 'password' not in request.data:
                return Response({'error': "Password is not provided"})

            serialized = CustomUserSerializer(user, data=request.data, partial=True)

            if serialized.is_valid():
                serialized.save()

                Log(f"{request.user.email} has updated own password").save()

                return Response({"msg": "Your password is updated."})
        
            return Response({"error": "There is some issue. Please try again."})

        except Exception as e:
            return Response(e)

class DeleteUserView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        try:
            if not request.user.is_superuser:
                return Response({"msg": "You are not admin to process it."})
                
            if 'email' not in request.data:
                return Response({"error": "Required data is not fulfiled. Please try again."})

            if not CustomUser.objects.filter(email=request.data['email']).exists():
                return Response({"error": "No such user exists."})
            
            CustomUser.objects.get(email=request.data['email']).delete()
            
            Log(log=f"{request.user.email} has deleted {request.data['email']} user.").save()

            return Response({"msg": "The user is deleted."})
                
        except Exception as e:
            return Response(e)
