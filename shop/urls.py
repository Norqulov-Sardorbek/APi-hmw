from django.urls import path
from shop.views import *

urlpatterns = [
    path('categories/', CategoryViewSet.as_view(), name='category-list'),
    path('courses/', CourseViewSet.as_view(), name='course-list'),
    path('courses/<int:category_id>/', CourseListByCategoryAPI.as_view(), name='course-list-by-category'),
    path('groups/', GroupViewSet.as_view(), name='group-list'),
    path('groups/<int:course_id>/', GroupViewSet.as_view(), name='group-list-by-course'),
    path('modules/', ModuleViewSet.as_view(), name='module-list'),
    path('modules/<int:group_id>/', ModuleViewSet.as_view(), name='module-list-by-group'),
    path('create-module/<int:group_id>/', ModuleCreateAPIView.as_view(), name='create-module'),
    path('homework/', HomeworkViewSet.as_view(), name='homework-list'),
    path('homework/<int:pk>/', HomeworkViewSet.as_view(), name='homework-detail'),
    path('create-homework/<int:module_id>/', HomeworkCreateAPIView.as_view(), name='create-homework'),
    path('students/<int:group_id>/', StudentViewSet.as_view(), name='student-list-by-group'),
    path('students/<int:group_id>/<int:pk>/', StudentViewSet.as_view(), name='student-detail'),
    path('teachers/', TeacherViewSet.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherViewSet.as_view(), name='teacher-detail'),
]
