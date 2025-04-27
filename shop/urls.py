from django.urls import path
from shop.views import *

urlpatterns = [
    path('categories/', CategoryViewSet.as_view()),
    path('courses/', CourseViewSet.as_view()),
    path('courses/<int:category_id>/', CourseListByCategoryAPI.as_view()),
    path('groups/<int:course_id>/', GroupViewSet.as_view()),
    path('modules/<int:group_id>/', ModuleViewSet.as_view()),
    path('homework/', HomeworkViewSet.as_view()),
    path('homework/<int:pk>/', HomeworkViewSet.as_view()),
    path('students/<int:group_id>/', StudentViewSet.as_view()),
    path('students/<int:group_id>/<int:pk>/', StudentViewSet.as_view()),
    path('teachers/', TeacherViewSet.as_view()),
    path('teachers/<int:pk>/', TeacherViewSet.as_view()),
]
