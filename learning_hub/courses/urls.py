from django.urls import path
from .views import CourseListLatestApi, CourseListApi, CourseDetailApi

urlpatterns = [
    path("", CourseListLatestApi.as_view(), name="latest-course"),
    path("courses/", CourseListApi.as_view(), name="course-list"),
    path("courses/<slug:slug>/", CourseDetailApi.as_view(), name="course-detail")
]
