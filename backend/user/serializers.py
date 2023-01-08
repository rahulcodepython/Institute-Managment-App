from rest_framework import serializers
from user.models import Teacher, Student, CustomUser, Staff, WaitingApproval

# Profile Button Serializer for Teacher, Student, Staff
class ProfileButtonTeacherSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField('get_position')
    email = serializers.StringRelatedField(source='teacherUser.email')
    name = serializers.SerializerMethodField('get_name')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Teacher
        fields = ['email', 'name', 'image', 'position']

    def get_position(self, obj):
        return CustomUser.objects.get(email=obj.teacherUser).position

    def get_name(self, obj):
        return Teacher.objects.get(teacherUser=obj.teacherUser).teacherName

    def get_image(self, obj):
        return Teacher.objects.get(teacherUser=obj.teacherUser).teacherImage.url

class ProfileButtonStudentSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField('get_position') 
    email = serializers.StringRelatedField(source='studentUser.email')
    name = serializers.SerializerMethodField('get_name')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Student
        fields = ['email', 'name', 'image', 'position']

    def get_position(self, obj):
        return CustomUser.objects.get(email=obj.studentUser).position

    def get_name(self, obj):
        return Student.objects.get(studentId=obj.studentId).studentName
        
    def get_image(self, obj):
        return Student.objects.get(studentId=obj.studentId).studentImage.url

class ProfileButtonStaffSerializer(serializers.ModelSerializer):

    position = serializers.SerializerMethodField('get_position') 
    email = serializers.StringRelatedField(source='staffUser.email')
    name = serializers.SerializerMethodField('get_name')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Staff
        fields = ['email', 'name', 'image', 'position']

    def get_position(self, obj):
        return CustomUser.objects.get(email=obj.staffUser).position

    def get_name(self, obj):
        return Staff.objects.get(staffUser=obj.staffUser).staffName

    def get_image(self, obj):
        return Staff.objects.get(staffUser=obj.staffUser).staffImage.url

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
        exclude = ['studentBio', 'studentRemarks']

# Register New User
class RegisterUserToCustomUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'position']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(email=self.validated_data['email'], position=self.validated_data['position'])
        password = self.validated_data['password']
        user.set_password(password)
        user.name = self.validated_data['email'].split('@')[0]
        user.save()
        
        return user

# Register New User
class WaitForApprovalRegisterUserToCustomUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaitingApproval
        fields = ['email', 'password', 'position']

# Show Profile for Teacher, Student, Staff private
class ShowProfileTeacherPrivateSerializer(serializers.ModelSerializer):

    teacherUser = serializers.StringRelatedField(source="teacherUser.email")

    class Meta:
        model = Teacher
        fields = '__all__'

class ShowProfileStudentPrivateSerializer(serializers.ModelSerializer):
    
    studentUser = serializers.StringRelatedField(source="studentUser.email")
    
    class Meta:
        model = Student
        fields = '__all__'

class ShowProfileStaffPrivateSerializer(serializers.ModelSerializer):

    staffUser = serializers.StringRelatedField(source="staffUser.email")

    class Meta:
        model = Staff
        fields = '__all__'