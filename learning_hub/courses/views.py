from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

from .models import Course

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
        courses = Course.objects.select_related('category').all()
        data = self.OutputSerializer(courses, many=True).data

        return Response(data)
