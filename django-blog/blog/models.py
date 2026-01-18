from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150, default="This is a default post")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
