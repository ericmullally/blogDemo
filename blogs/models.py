from django.db import models


class BlogPost(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    body = models.CharField(max_length=5000)
    img = models.CharField(max_length=100)
