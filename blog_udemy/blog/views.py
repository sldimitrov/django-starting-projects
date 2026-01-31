from datetime import date

from django.shortcuts import render, get_object_or_404
from .models import Post

def get_date(post):
    return post.date

def get_post(slug):
    all_posts = Post.objects.all()

    for post in all_posts:
        if post.slug == slug:
            return post
    return None

# Create your views here.
def starting_page(request):
    all_posts = Post.objects.all().order_by("date").order_by("-date")[:3]

    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": all_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": Post.objects.all()
    })

def post_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.caption.all()
    })
