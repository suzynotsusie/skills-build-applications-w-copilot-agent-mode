from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(required=False)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(required=False)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'score', 'last_updated']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(required=False)

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty', 'duration']