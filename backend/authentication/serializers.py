from rest_framework import serializers
from authentication.models import Staff, Student, Teacher, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # image = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password', 'aboutme', 'gender', 'mobile', 'position']

    # def get_image(self):
    #     return self.image.url

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['domain', 'subdomain']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['standard', 'domain']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['dept']