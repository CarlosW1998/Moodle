#Django Imports 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny 
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
#App Imports
from forum.models import Forum, Comentary, Question
from forum.serializers import NewComentarySerializer, NewForumSerializer,\
    NewQuestionSerializer, ComentarySerializer, ForumSerializer, \
        QuestionSerializer

class ForumViewset(viewsets.GenericViewSet):
    querryset = Forum.objects.all()
    serializer_class = ForumSerializer
    parser_classes = (FormParser, JSONParser, MultiPartParser)
    
    @action(methods=['post'], url_path='question', detail=False)
    def createQuestion(self, request):
        data = request.data.dict()
        data['owner'] = request.user.id
        serializer = NewQuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], url_path='comentary', detail=False)
    def createComentary(self, request):
        data = request.data.dict()
        data['owner'] = request.user.id
        serializer = NewComentarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)

    
        


