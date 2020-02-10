from django.db import models
from classroom.models import Classroom
# Create your models here.

class Post(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pubDate = models.DateField(auto_now_add=True)

class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    binary = models.TextField(null=True, blank=True)

