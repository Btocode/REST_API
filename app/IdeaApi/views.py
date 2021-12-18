from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.serializers import Serializer

from .models import Idea, Suggestion, User
from .serializers import ideaSerializer, suggSerializer, userSerializer


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

# IdeaViews class

class IdeaGroup1(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Idea.objects.all()
    serializer_class = ideaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Group2 has the ability to view individual data, delete and update data 
class IdeaGroup2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Idea.objects.all()
    serializer_class = ideaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class SuggestionsGroup1(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Suggestion.objects.all()
    serializer_class = suggSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SuggestionsGroup2(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Suggestion.objects.all()
    serializer_class = suggSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)