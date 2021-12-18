from django.db import models
from rest_framework import fields, serializers
from .models import Suggestion, User,Idea

class userSerializer(serializers.ModelSerializer):
  class Meta():
    model = User
    fields = ('firstName','lastName')

class suggSerializer(serializers.ModelSerializer):
  class Meta():
    model = Suggestion
    fields = ('ideaId','content')
class ideaSerializer(serializers.ModelSerializer):
  user = userSerializer(many=False)
  class Meta():
    model = Idea
    fields = ('ideaId','ideaDesc','ideatitle','ideatags','upVotes','downVotes','user')

