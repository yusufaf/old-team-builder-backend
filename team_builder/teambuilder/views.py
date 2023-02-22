from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer, TeamSerializer, GroupSerializer
from .models import Team


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer