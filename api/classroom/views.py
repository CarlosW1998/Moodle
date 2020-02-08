#Django imports
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny 
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction

#App Imports
from forum.models import Forum
from forum.serializers import NewForumSerializer
from classroom.models import Classroom, UserClassRoomRelation
from classroom.serializers import NewClassroomSerializer, \
     ClassroomSerializer, UserClassRoomRelationSerializer, \
          NewUserClassRoomRelationSerializer


class ClassroomViewset(viewsets.GenericViewSet):
    querryset = Classroom.objects.all()
    serializer_class = NewClassroomSerializer
    parser_classes = (FormParser, JSONParser, MultiPartParser)

#    @action(methods=['post'], url_path='', detail=False)
    def create(self, request):
        newF  = Forum(name='Test')
        newF.save()
        if not type(request.data) == dict:data = request.data.dict()
        else: data = request.data
        data['owner'] = request.user.pk
        data['forum'] = newF.id
        serializer =NewClassroomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            newF.name = serializer.data['name']
            newF.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        newF.delete()
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['get'], url_path='join', detail=True)
    def join(lsef, request, pk=None):
        classroom = get_object_or_404(Classroom, uniqueCode=pk)
        serializer = NewUserClassRoomRelationSerializer(
            data={'classroom': classroom.id, 'user': request.user.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        querryset = Classroom.objects.filter(owner=request.user.id)
        serializer = ClassroomSerializer(querryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], url_path='student', detail=False)
    def student(lsef, request):
        querryset = UserClassRoomRelation.objects.filter(user=request.user.id)
        querryset = [i.classroom for i in querryset]
        serializer = ClassroomSerializer(querryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
