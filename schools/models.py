from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    grades = models.CharField(max_length=200, default="Ask office for grades")
    image = models.ImageField(upload_to='schools/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class New(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=20, default="for_post_identification")
    date = models.DateTimeField(default=timezone.now)
    script = models.TextField(max_length=20000)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

