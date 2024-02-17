import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializer import PostRequestSerializer, UserResponseSerializer, PatchRequestSerializer, LoginSerializer
from utils.utils import checkLoggedIn, get_request_body, get_response

#Make a user and retrieve all the users
class usersManager(APIView):
    def post(self, request):
        try:
            checkLoggedIn(request)
            user = get_request_body(request, PostRequestSerializer)
            new_user = User.objects.create_user(**user)
            new_user.save()
            responseSerializer = UserResponseSerializer( data = new_user.__dict__ )
            return get_response(responseSerializer)
        
        except Exception as exp:
            return Response(str(exp), status = 500 )
    
    def get(self, request):
        try:
            checkLoggedIn(request)
            users = [user.__dict__ for user in list(User.objects.all())]
            responseSerializer = UserResponseSerializer(data = users, many = True)
            return get_response(responseSerializer)
        
        except Exception as exp:
            return Response(str(exp), status = 500 )


class userManager(APIView):
    def get(self, request, userId):
        try:
            checkLoggedIn(request)
            user = User.objects.get(id = userId).__dict__
            responseSerializer = UserResponseSerializer( data = user )
            return get_response(responseSerializer)
        
        except Exception as exp:
            return Response(str(exp), status = 500 )

    def patch(self, request, userId):
        try:
            checkLoggedIn(request)
            userData = get_request_body(request, PatchRequestSerializer)
            user = User.objects.get( id = userId )
            for key,value in userData.items():
                setattr(user, key, value)
            user.save()
            responseSerializer = UserResponseSerializer( data = user.__dict__ )
            return get_response(responseSerializer)
        
        except Exception as exp:
            return Response(str(exp), status = 500 )
    
    def delete(self, request, userId):
        try: 
            checkLoggedIn(request)
            user = User.objects.get( id = userId )
            response = user.delete()
            return Response(response[0])
        
        except Exception as exp:
            return Response(str(exp), status = 500 )



class LoginManager(APIView):
    def post(self, request):
        try:
            body = get_request_body(request, LoginSerializer)
            user = authenticate(request, **body)
            if user is not None:
                login(request, user)
                return Response("LoggedIn")
            else:
                return Response("Not authenticated")
        except Exception as exp:
            return Response(str(exp), status = 500 )
    
    def delete(self, request):
        try: 
            logout(request)
            return Response("Logged out")
        except Exception as exp:
            return Response(str(exp), status = 500 )