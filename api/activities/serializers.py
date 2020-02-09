from activities.models import Activity, File, Answer, AnswerFile
from users.serializers import UserSerializer
from rest_framework import serializers

class NewActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','classroom', 'text', 'pubDate', 'deadline']

class NewFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id','activity', 'filename', 'binary']

class NewAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [ 'id','activity', 'owner', 'postDate', 'comentary']

class NewAnswerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerFile
        fields = ['id','answer', 'filename', 'binary']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'filename', 'binary']

class AnswerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerFile
        fields = ['id','filename', 'binary']

class AnswerSerializer(serializers.ModelSerializer):
    Owner = UserSerializer(source='owner', many=False, read_only=True)    
    files = serializers.SerializerMethodField()
    class Meta:
        model = Answer
        fields = [ 'id', 'score', 'postDate', 'comentary', 'Owner', 'files']

    def get_files(self, instance):
        querryset = AnswerFile.objects.filter(answer=instance.id)
        serializer = AnswerFileSerializer(querryset, many=True)
        return serializer.data


class ActivitySerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()
    class Meta:
        model = Activity
        fields = ['id', 'text', 'pubDate', 'deadline', 'files', 'answers']
    
    def get_files(self, instance):
        querryset = File.objects.filter(activity=instance.id)
        serializer = FileSerializer(querryset, many=True)
        return serializer.data

    def get_answers(self, instance):
        querryset = Answer.objects.filter(activity=instance.id)
        serializer = AnswerSerializer(querryset, many=True)
        return serializer.data