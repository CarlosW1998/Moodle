from django.db import models
from classroom.models import Classroom
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pubDate = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True)

class File(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    binary = models.TextField(null=True, blank=True)

class Answer(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    postDate = models.DateField(auto_now_add=True)
    comentary = models.CharField(max_length=100)

class AnswerFile(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    binary = models.TextField(null=True, blank=True)