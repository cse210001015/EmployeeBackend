from rest_framework import serializers

class PostRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    salary = serializers.IntegerField()
    age = serializers.IntegerField()
    position = serializers.CharField()
    department = serializers.CharField()

class EmployeeResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    salary = serializers.IntegerField()
    age = serializers.IntegerField()
    position = serializers.CharField()
    department = serializers.CharField()

class PatchRequestSerializer(serializers.Serializer):
    name = serializers.CharField( required = False )
    salary = serializers.IntegerField( required = False )
    age = serializers.IntegerField( required = False )
    position = serializers.CharField( required = False )
    department = serializers.CharField( required = False )