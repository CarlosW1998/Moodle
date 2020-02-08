
from rest_framework import serializers
from classroom.models import Classroom, UserClassRoomRelation
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.validators import UniqueTogetherValidator
from forum.serializers import ForumSerializer

class NewUserClassRoomRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClassRoomRelation
        fields = ['classroom', 'user']
        validators=[
            UniqueTogetherValidator(
                queryset=UserClassRoomRelation.objects.all(),
                fields=['classroom', 'user']
                )
        ]

class UserClassRoomRelationSerializer(serializers.ModelSerializer):
    User = UserSerializer(many=False,read_only=True, source='user')
    class Meta:
        model = UserClassRoomRelation
        fields = ['User']

class ClassroomSerializer(serializers.ModelSerializer):
    Owner = UserSerializer(many=False,read_only=True, source='owner')
    users = serializers.SerializerMethodField()
    Forum = ForumSerializer(source='forum', read_only=True, many=False)

    class Meta:
        model = Classroom
        fields = ['Owner', 'Forum', 'name','uniqueCode', 'users']

    def get_users(self, instance):
        querryset = UserClassRoomRelation.objects.filter(classroom=instance.id)
        serializers = UserClassRoomRelationSerializer(
            querryset, many=True)
        return serializers.data

class NewClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['owner', 'name', 'uniqueCode', 'forum']
