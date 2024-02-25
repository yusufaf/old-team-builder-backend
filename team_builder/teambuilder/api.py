from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from nba_api.stats.endpoints import playercareerstats



class GetPlayerCareerStats(APIView):    
    def get(self, request, format=None):
        player_id = request.GET.get('player_id')
        
        career = playercareerstats.PlayerCareerStats(player_id='2544')
        career.get_json()





class ListPlayers(APIView):
    """
    View to list all players
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """