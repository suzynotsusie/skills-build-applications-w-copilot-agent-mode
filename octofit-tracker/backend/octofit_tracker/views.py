from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.conf import settings
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    # Get the current host from the request
    host = request.get_host()
    protocol = 'https' if request.is_secure() else 'http'
    base_url = f"{protocol}://{host}"
    
    return Response({
        'users': f"{base_url}/api/users/",
        'teams': f"{base_url}/api/teams/",
        'activities': f"{base_url}/api/activities/",
        'leaderboard': f"{base_url}/api/leaderboard/",
        'workouts': f"{base_url}/api/workouts/",
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer