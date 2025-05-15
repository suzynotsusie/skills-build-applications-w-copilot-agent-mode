from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.team = Team.objects.create(
            name='Test Team'
        )
        
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration=timedelta(minutes=30)
        )
        
        self.leaderboard = Leaderboard.objects.create(
            user=self.user,
            score=100
        )
        
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='Test workout description',
            difficulty='medium',
            duration=timedelta(minutes=45)
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.activity_type, 'running')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user, self.user)
        self.assertEqual(self.leaderboard.score, 100)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'medium')

class APITests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        self.user = User.objects.create(**self.user_data)

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)