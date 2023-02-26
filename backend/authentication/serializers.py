from rest_framework import serializers
from authentication.models import Staff, Student, Teacher, CustomUser, Employee

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    joininDate = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    # image = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        exclude = ['groups', 'user_permissions', 'id']

    # def get_image(self):
    #     return self.image.url

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)

        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
            
        return user

class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.email')
    salary = serializers.IntegerField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

class TeacherSerializer(EmployeeSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StaffSerializer(EmployeeSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.email', read_only=True)
    is_session_active = serializers.BooleanField(read_only=True)
    is_fees_clear = serializers.BooleanField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'