from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from staff.serializers import ShowTeachersSerializer, ShowStaffSerializer, ShowStudentSerializer
from authentication.models import CustomUser

# Create your views here.

class ShowTeachersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            if not request.user.is_superuser:
                return Response({"error": "You are not admin to process it."})

            return Response(ShowTeachersSerializer(CustomUser.objects.filter(is_active=True).filter(position='Teacher'), many=True).data)
        except Exception as e:
            return Response(e)

class ShowStaffsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            if not request.user.is_superuser:
                return Response({"error": "You are not admin to process it."})

            return Response(ShowStaffSerializer(CustomUser.objects.filter(is_active=True).filter(position='Staff'), many=True).data)
        except Exception as e:
            return Response(e)

class ShowStudentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            if not request.user.is_superuser:
                return Response({"error": "You are not admin to process it."})

            return Response(ShowStudentSerializer(CustomUser.objects.filter(is_active=True).filter(position='Student'), many=True).data)
        except Exception as e:
            return Response(e)

class ShowInactiveUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            if not request.user.is_superuser:
                return Response({"error": "You are not admin to process it."})

            return Response({
                "teachers": ShowTeachersSerializer(CustomUser.objects.filter(is_active=False).filter(position='Teacher'), many=True).data,
                "staffs": ShowStaffSerializer(CustomUser.objects.filter(is_active=False).filter(position='Staff'), many=True).data,
                "students": ShowStudentSerializer(CustomUser.objects.filter(is_active=False).filter(position='Student'), many=True).data
            })
        except Exception as e:
            return Response(e)