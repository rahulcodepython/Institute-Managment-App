from rest_framework import serializers
from user.models import Teacher, Student, CustomUser, Staff

# Profile Button Serializer for Teacher, Student, Staff
class ProfileButtonTeacherSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField('get_position')
    email = serializers.StringRelatedField(source='teacherUser.email')
    name = serializers.SerializerMethodField('get_name')
    userId = serializers.SerializerMethodField('get_userId')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Teacher
        fields = ['userId', 'email', 'name', 'image', 'position']

    def get_position(self, obj):
        return CustomUser.objects.get(email=obj.teacherUser).position
    def get_name(self, obj):
        return Teacher.objects.get(teacherId=obj.teacherId).teacherName
    def get_userId(self, obj):
        return Teacher.objects.get(teacherId=obj.teacherId).teacherId
    def get_image(self, obj):
        return Teacher.objects.get(teacherId=obj.teacherId).teacherImage.url

class ProfileButtonStudentSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField('get_position') 
    email = serializers.StringRelatedField(source='studentUser.email')
    name = serializers.SerializerMethodField('get_name')
    userId = serializers.SerializerMethodField('get_userId')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Student
        fields = ['userId', 'email', 'name', 'image', 'position']

    def get_position(self, obj):
        return CustomUser.objects.get(email=obj.studentUser).position
    def get_name(self, obj):
        return Student.objects.get(studentId=obj.studentId).studentName
    def get_userId(self, obj):
        return Student.objects.get(studentId=obj.studentId).studentId
    def get_image(self, obj):
        return Student.objects.get(studentId=obj.studentId).studentImage.url

class ProfileButtonStaffSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField('get_position') 
    email = serializers.StringRelatedField(source='staffUser.email')
    name = serializers.SerializerMethodField('get_name')
    userId = serializers.SerializerMethodField('get_userId')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Staff
        fields = ['userId', 'email', 'name', 'image', 'position']

    def get_position(self, obj):
        return CustomUser.objects.get(email=obj.staffUser).position
    def get_name(self, obj):
        return Staff.objects.get(staffId=obj.staffId).staffName
    def get_userId(self, obj):
        return Staff.objects.get(staffId=obj.staffId).staffId
    def get_image(self, obj):
        return Staff.objects.get(staffId=obj.staffId).staffImage.url

# Show Teachers data for Admin
class ShowTeachersSerializer(serializers.ModelSerializer):

    teacherUser = serializers.StringRelatedField(source='teacherUser.email')

    class Meta:
        model = Teacher
        exclude = ['teacherBio']

# Show Students data for Admin
class ShowStudentsSerializer(serializers.ModelSerializer):

    studentUser = serializers.StringRelatedField(source='studentUser.email')

    class Meta:
        model = Student
        exclude = ['studentBio', 'studentRemarks', ]

# Register New User
class RegisterUserToCustomUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

# Show Profile for Teacher, Student, Staff private
class ShowProfileTeacherPrivateSerializer(serializers.ModelSerializer):

    teacherUser = serializers.StringRelatedField(source="teacherUser.email")

    class Meta:
        model = Teacher
        exclude = ['teacherId']

class ShowProfileStudentPrivateSerializer(serializers.ModelSerializer):
    
    studentUser = serializers.StringRelatedField(source="studentUser.email")
    
    class Meta:
        model = Student
        exclude = ['studentId']

class ShowProfileStaffPrivateSerializer(serializers.ModelSerializer):

    staffUser = serializers.StringRelatedField(source="staffUser.email")

    class Meta:
        model = Staff
        exclude = ['staffId']