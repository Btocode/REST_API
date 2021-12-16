from django.db import models
from rest_framework import fields, serializers
from .models import User,Idea

class userSerializer(serializers.ModelSerializer):
  class Meta():
    model = User
    fields = '__all__'

class ideaSerializer(serializers.ModelSerializer):
  class Meta():
    model = Idea
    fields = '__all__'
