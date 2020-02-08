from rest_framework import serializers
from django.contrib.auth.models import User

class NewUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_date) :
        user = super(NewUserSerializer, self).create(validated_date)
        user.set_password(validated_date['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']