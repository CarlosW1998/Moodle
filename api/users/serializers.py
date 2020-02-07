from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_date) :
        user = super(UserSerializer, self).create(validated_date)
        user.set_password(validated_date['password'])
        user.save()
        return user
