from rest_framework import serializers
from authentication.models import Teacher, Staff, Student, CustomUser
from authentication.serializers import TeacherSerializer, StaffSerializer, StudentSerializer

class ShowTeachersSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        exclude = ['groups', 'user_permissions', 'id', 'password']

    def get_teacher(self, obj):
        return TeacherSerializer(Teacher.objects.get(user=obj)).data

class ShowStaffSerializer(serializers.ModelSerializer):
    staff = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        exclude = ['groups', 'user_permissions', 'id', 'password']

    def get_staff(self, obj):
        return StaffSerializer(Staff.objects.get(user=obj)).data

class ShowStudentSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        exclude = ['groups', 'user_permissions', 'id', 'password']

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(user=obj)).data