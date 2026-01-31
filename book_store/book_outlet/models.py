from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Author - {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=3)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=True)

    def __str__(self):
        return f"{self.title} - {self.author} with rating of {self.rating}"


