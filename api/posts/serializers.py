from rest_framework import serializers
from posts.models import Post, File

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'classroom', 'text', 'pubDate']

class NewFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'post', 'filename', 'binary']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'filename', 'binary']

class PostSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'text', 'pubDate','files']
    
    def get_files(self, instance):
        querryset = File.objects.filter(post = instance.id)
        serializer = FileSerializer(querryset, many=True)
        return serializer.data


