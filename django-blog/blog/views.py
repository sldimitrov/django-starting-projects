from django.http import HttpResponse, JsonResponse

from .models import Post

def index(request):
    posts = Post.objects.all()

    data = [
        {
            "title": post.title,
            "text": post.text
        }
        for post in posts
    ]

    return JsonResponse(data, safe=False)

def detail(request, title):
    return HttpResponse("You're looking at posts %s." % title)


def category(request, category_id):
    response = "You're looking at the category of post %s."
    return HttpResponse(response % category_id)


def tag(request, tag_id):
    return HttpResponse("You're seeing tag %s." % tag_id)
