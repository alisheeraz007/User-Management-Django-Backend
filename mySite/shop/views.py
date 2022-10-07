from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User as Userr
from .serializers import UserSerializer

class User(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        users = Userr.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''

        data= {
                "user_name": request.data.get('user_name'),
                "user_email": request.data.get('user_email'),
                "age": request.data.get('age'),
                "additionalInfo": request.data.get('additionalInfo'),
                "dateOfBirth": request.data.get('dateOfBirth'),
                "profileImage": request.data.get('profileImage'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Added")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)