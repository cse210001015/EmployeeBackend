from rest_framework import serializers
from django.contrib.auth.models import User

class PostRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

class UserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()

class PatchRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField( required = False )
    last_name = serializers.CharField(required = False)
    email = serializers.CharField(required = False)
    username = serializers.CharField(required = False)
    password = serializers.CharField(required = False)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()