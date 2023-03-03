from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListPlayers(APIView):
    """
    View to list all players
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """