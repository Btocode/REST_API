from django.conf import UserSettingsHolder
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import authentication
from rest_framework import permissions
from .serializers import userSerializer
from .models import User
from rest_framework import status,viewsets

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Create your views here.


class userAPI(APIView):
    def get(self, request, format=None, pk=None):
        id = pk
        if id is not None:
            usr = User.objects.get(userId=id)
            serializer = userSerializer(usr)
            return Response(serializer.data)
        usr = User.objects.all()
        serializer = userSerializer(usr, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "data created"})
        return Response(serializer.errors)

    def put(self, request, format=None, pk=None):
        id = pk
        usr = User.objects.get(pk=id)
        serializer = userSerializer(usr, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None, pk=None):
        id = pk
        usr = User.objects.get(pk=id)
        serializer = userSerializer(usr, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Data Updated"})
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, pk=None):
        id = pk
        usr = User.objects.get(userId=id)
        usr.delete()
        return Response({"msg": "data Deleted"})

