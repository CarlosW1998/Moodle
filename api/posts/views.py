#Django Imports 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny 
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
#App Imports
from posts.permissions import IsOwner
from posts.models import Post, File
from classroom.models import Classroom
from posts.serializers import NewFileSerializer, NewPostSerializer, \
    FileSerializer, PostSerializer

class PostsViewset(viewsets.GenericViewSet):
    permission_classes = [IsOwner]
    querryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (FormParser, JSONParser, MultiPartParser)

    @action(methods=['post'], url_path='post', detail=False)
    def createPost(self, request):
        if not type(request.data) == dict:data = request.data.dict()
        else: data = request.data
        try:
            data['classroom'] = Classroom.objects.get(uniqueCode=data['classroom']).id
        except:
            return Response('Ivalid Classroom', status=status.HTTP_400_BAD_REQUEST)
        serializer = NewPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            savedfiles = []
            if 'files' in data.keys():
                for i in data['files']:
                    serializerFile = NewFileSerializer(data=i)
                    if serializerFile.is_valid():
                        serializerFile.save()
                        savedfiles.append(serializerFile.data)
                    else: savedfiles.append(serializerFile.errors)
                responsedata = serializer.data
                responsedata['files'] = savedfiles
            return Response(responsedata,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


