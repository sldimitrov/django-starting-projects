from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.EmailField(max_length=254)

class Tag(models.Model):
    caption = models.CharField(max_length=150)

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image_name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    caption = models.ManyToManyField(Tag)
    date = models.DateField()
    slug = models.SlugField()
    content = models.CharField(max_length=1000)
