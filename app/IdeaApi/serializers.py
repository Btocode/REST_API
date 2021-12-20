from django.db import models
from rest_framework import fields, serializers
from .models import Suggestion, User,Idea


# I have changed this section for testing purpose 19.12.21
class userSerializer(serializers.ModelSerializer):
  class Meta():
    model = User
    fields = ('firstName','lastName','email','password','age','gender')

class LoginSerializer(serializers.ModelSerializer):
  class Meta():
    model = User
    fields = ('email',"password")
class suggSerializer(serializers.ModelSerializer):
  class Meta():
    model = Suggestion
    fields = ('ideaId','content')
class ideaSerializer(serializers.ModelSerializer):
  user = userSerializer(many=False)
  class Meta():
    model = Idea
    fields = ('ideaId','ideaDesc','ideatitle','ideatags','upVotes','downVotes','user')

