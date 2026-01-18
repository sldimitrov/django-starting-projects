from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:title>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:category>/category/", views.category, name="category"),
    # ex: /polls/5/vote/
    path("<int:tag_id>/tag/", views.tag, name="tag"),
]
