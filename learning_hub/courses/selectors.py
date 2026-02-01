from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from .models import Course

def latest_course_list() -> QuerySet[Course]:
    return Course.objects.select_related('category').all().order_by("-started_at")

def course_list() -> QuerySet[Course]:
    return Course.objects.select_related('category').all()

def course_get(*, slug: str) -> Course:
    return get_object_or_404(Course, slug=slug)
