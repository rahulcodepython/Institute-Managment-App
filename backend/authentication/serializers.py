from rest_framework import serializers
from authentication.models import Staff, Student, Teacher, UnapprovedUser, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password']

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)

        if 'password' in validated_data.keys():
            user.set_password(validated_data['password'])
            user.save()
            return user

class UnapprovedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnapprovedUser
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='teacherUser.name')
    email = serializers.StringRelatedField(source='teacherUser.email')
    joiningDate = serializers.StringRelatedField(source='teacherUser.joiningDate')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Teacher
        fields = '__all__'

    def get_image(self, obj):
        return Teacher.objects.get(teacherUser=obj.teacherUser).teacherImage.url

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='studentUser.name')
    email = serializers.StringRelatedField(source='studentUser.email')
    joiningDate = serializers.StringRelatedField(source='studentUser.joiningDate')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Student
        fields = '__all__'

    def get_image(self, obj):
        return Student.objects.get(studentUser=obj.studentUser).studentImage.url

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class StaffSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='staffUser.name', read_only=True)
    email = serializers.StringRelatedField(source='staffUser.email', read_only=True)
    joiningDate = serializers.StringRelatedField(source='staffUser.joiningDate', read_only=True)
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Staff
        fields = '__all__'

    def get_image(self, obj):
        return Staff.objects.get(staffUser=obj.staffUser).staffImage.url

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)