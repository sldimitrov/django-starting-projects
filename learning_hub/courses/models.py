from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.label

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    started_at = models.DateField()
    finished_at = models.DateField()
    slug = models.SlugField()

    def __str__(self):
        return self.title



class Module(models.Model):
    topic = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.topic

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# class Enrollment(models.Model):
#     pass
#
# class UserProgress(models.Model):
#     pass
