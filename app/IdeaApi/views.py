from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import User, Idea
from .serializers import userSerializer, ideaSerializer 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin,UpdateModelMixin,DestroyModelMixin


# Group1 has the ability to view and create data 
class Group1(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = userSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Group2 has the ability to view individual data, delete and update data 
class Group2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = userSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    