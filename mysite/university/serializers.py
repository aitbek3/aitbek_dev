from rest_framework import serializers
from .models import *
from .models import Role
from django.contrib.auth import get_user_model


class UserProfileProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfileProfessor
        fields = '__all__'


class UserProfileStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfileStudent
        fields = '__all__'


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class HomeworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class SubmittingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submitting
        fields = '__all__'


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)
    role_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'role_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_name = validated_data.pop('role')
        role_password = validated_data.pop('role_password')

        try:
            role = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            raise serializers.ValidationError('Invalid role.')

        if role.password != role_password:
            raise serializers.ValidationError('Incorrect role password.')

        user = User.objects.create_user(**validated_data, role=role)
        return user