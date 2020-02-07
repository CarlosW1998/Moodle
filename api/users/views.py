#Django imports
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny 
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
#app Imports
from users.serializers import UserSerializer
# Create your views here.
class AuthVeiwset(viewsets.GenericViewSet):
    #authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    serializer_class = UserSerializer
    parser_classes = (FormParser, JSONParser, MultiPartParser)
    
    
    @action(methods=['post'], url_path='createuser', detail=False)
    def createuser(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)