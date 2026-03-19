from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, team)

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, description='Test Activity', duration=10)
        self.assertEqual(activity.description, 'Test Activity')
        self.assertEqual(activity.duration, 10)
        self.assertEqual(activity.user, user)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', reps=5)
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.reps, 5)

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.team, team)
        self.assertEqual(leaderboard.points, 50)
