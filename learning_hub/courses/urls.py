from django.urls import path
from .views import CourseListApi

urlpatterns = [
    path("courses/", CourseListApi.as_view(), name="course-list"),
]
