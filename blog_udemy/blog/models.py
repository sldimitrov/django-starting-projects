from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.EmailField(max_length=254, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=150)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image_name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    caption = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=50, db_index=True)
    content = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} with Author - '{self.author}'"
