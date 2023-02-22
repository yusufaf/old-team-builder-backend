from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Team

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# This code specifies the model to work with and the fields to be converted to JSON.
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'createdAt', 'updatedAt']
