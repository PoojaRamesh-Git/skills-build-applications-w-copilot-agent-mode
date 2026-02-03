from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=30, date=date.today())
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.type, 'Test Activity')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.user, self.user)
        self.assertEqual(self.leaderboard.score, 100)
