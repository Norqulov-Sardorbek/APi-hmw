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
    class Meta:
        model = Module
        fields = ["id","title","is_given","get_video","get_students"]
    def get_video(self, instance):
        return instance.video.url
    def get_students(self, instance):
        return instance.group.students.count()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id","name","started_at","ended_at","status"]


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ["id","oveview","get_file","dedline"]
    def get_file(self, instance):
        return instance.file.url

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id","first_name","last_name","gender","phone_number","password","get_image","student_code"]
    def get_image(self, instance):
        return instance.image.url


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id","first_name","last_name","phone_number","password","get_image","username"]
    def get_image(self, instance):
        return instance.image.url
