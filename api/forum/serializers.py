from rest_framework import serializers
from forum.models import Forum, Question, Comentary

from django.contrib.auth.models import User
from users.serializers import UserSerializer


class NewForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'name']

class NewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'owner', 'forum', 'question', 'pubDate']    

class NewComentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentary
        fields = ['id', 'owner', 'question', 'comentary', 'pubDate']

class ComentarySerializer(serializers.ModelSerializer):
    Owner = UserSerializer(source='owner', many=False, read_only=True)
    class Meta:
        model = Comentary
        fields = ['id','comentary', 'pubDate', 'Owner']
    
class QuestionSerializer(serializers.ModelSerializer):
    Owner = UserSerializer(source='owner', many=False, read_only=True)
    answears = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['id', 'Owner','question','pubDate', 'answears']
    
    def get_answears(self, instance):
        querryset = Comentary.objects.filter(question=instance.id)
        serializer = ComentarySerializer(querryset, many=True)
        return serializer.data

class ForumSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    class Meta:
        model = Forum
        fields = ['id','name', 'questions']
    def get_questions(self, instance):
        querryset = Question.objects.filter(forum=instance.id)
        serializer = QuestionSerializer(querryset, many=True)
        return serializer.data
