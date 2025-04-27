from rest_framework import serializers
from shop.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ["id", "title", "is_given", "video", "student_count"]

    def get_video(self, instance):
        return instance.video.url if instance.video else None

    def get_student_count(self, instance):
        return instance.group.students.count()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", "started_at", "ended_at", "status"]


class HomeworkSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Homework
        fields = ["id", "overview", "file", "deadline"]

    def get_file(self, instance):
        return instance.file.url if instance.file else None


class StudentSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "phone_number", "password", "image", "student_code"]

    def get_image(self, instance):
        return instance.image.url if instance.image else None


class TeacherSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "phone_number", "password", "image", "username"]

    def get_image(self, instance):
        return instance.image.url if instance.image else None
