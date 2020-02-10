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
from classroom.models import Classroom
from activities.models import Activity, File, \
    Answer, AnswerFile
from activities.serializers import NewActivitySerializer, NewAnswerFileSerializer, \
    NewAnswerSerializer, NewFileSerializer, FileSerializer, AnswerFileSerializer, \
    AnswerSerializer, ActivitySerializer

class ActivityViewsets(viewsets.GenericViewSet):
    permission_classes = [IsOwner, IsAuthenticated]
    querryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    parser_classes = (FormParser, JSONParser, MultiPartParser)

    def create(self, request):
        if not type(request.data) == dict:data = request.data.dict()
        else: data = request.data
        
        try:
            print(Classroom.objects.get(uniqueCode=data['classroom']))
            data['classroom'] = Classroom.objects.get(uniqueCode=data['classroom']).id
        except:
            return Response('Ivalid Classroom', status=status.HTTP_400_BAD_REQUEST)
        serializer = NewActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if 'files' in data.keys():
                for i in data['files']:
                    i['activity'] = serializer.data['id']
                    serializerFile = NewFileSerializer(data=i)
                    if serializerFile.is_valid():
                        serializerFile.save()
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], url_path='setscore', detail=True)
    def setscore(self, request, pk=None):
        if pk == None:
            return Response("Invalid Score", status=status.HTTP_400_BAD_REQUEST)    
        answer = get_object_or_404(Answer, pk=pk)
        try:
            score = int(request.data['score'])
            if score > 10 or score < 0:
                raise Exception("Invalid Score")
        except:
            return Response("Invalid Score", status=status.HTTP_400_BAD_REQUEST)
        answer.score = score
        answer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



class AnswerViewset(viewsets.GenericViewSet):
    querryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    parser_classes = (FormParser, JSONParser, MultiPartParser)

    def create(self, request):
        if not type(request.data) == dict:data = request.data.dict()
        else: data = request.data
        try:
            data['owner'] = request.user.id
        except:
            return Response('Ivalid User', status=status.HTTP_400_BAD_REQUEST)
        serializer = NewAnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if 'files' in data.keys():
                for i in data['files']:
                    i['answer'] = serializer.data['id']
                    serializerFile = NewAnswerFileSerializer(data=i)
                    if serializerFile.is_valid():
                        serializerFile.save()
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)