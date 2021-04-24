from django.db import models


class School(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='schools/images')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.name


