from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .selectors import course_list, course_get, latest_course_list

class CourseListLatestApi(APIView):
    class OutputSerializer(serializers.Serializer):
        class CategorySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            label = serializers.CharField()

        title = serializers.CharField()
        description = serializers.CharField()
        category = CategorySerializer()
        started_at = serializers.DateField()
        finished_at = serializers.DateField()
        slug = serializers.SlugField()

    def get(self, request):
        courses = latest_course_list()
        data = self.OutputSerializer(courses, many=True).data

        return Response(data)

class CourseListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        class CategorySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            label = serializers.CharField()

        title = serializers.CharField()
        description = serializers.CharField()
        category = CategorySerializer()
        started_at = serializers.DateField()
        finished_at = serializers.DateField()
        slug = serializers.SlugField()

    def get(self, request):
        courses = course_list()
        data = self.OutputSerializer(courses, many=True).data

        return Response(data)


class CourseDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        class CategorySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            label = serializers.CharField()

        title = serializers.CharField()
        description = serializers.CharField()
        category = CategorySerializer()
        started_at = serializers.DateField()
        finished_at = serializers.DateField()
        slug = serializers.SlugField()

    def get(self, request, slug):
        course = course_get(slug=slug)
        data = self.OutputSerializer(course).data

        return Response(data)
