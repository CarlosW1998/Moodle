from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=200)

class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    pubDate = models.DateField(auto_now_add=True)

class Comentary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comentary = models.CharField(max_length=200)
    pubDate = models.DateField(auto_now_add=True)

