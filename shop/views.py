from rest_framework import generics,status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import *
from django.shortcuts import get_object_or_404


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return Course.objects.filter(category=category_id)


class CourseListByCategoryAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'category_id'


class GroupViewSet(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        return Group.objects.filter(course=course_id)


class ModuleViewSet(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_queryset(self):
        group_id = self.kwargs.get("group_id")
        return Module.objects.filter(group=group_id)
class ModuleCreateAPIView(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def post(self, request, *args, **kwargs):
        group_id = self.kwargs.get("group_id")
        group = get_object_or_404(Group, pk=group_id)

        data = request.data
        data['group'] = group.id

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeworkViewSet(generics.ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    def get_queryset(self):
        module_id = self.kwargs.get("module_id")
        return Homework.objects.filter(module=module_id)

class HomeworkCreateAPIView(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    def post(self, request, *args, **kwargs):
        module_id = self.kwargs.get("module_id")
        module = get_object_or_404(Module, pk=module_id)

        data = request.data
        data['module'] = module.id


        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        group_id = self.kwargs.get("group_id")
        return Student.objects.filter(group=group_id)



class TeacherViewSet(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
