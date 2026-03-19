from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User.objects.create(name='Batman', email='batman@dc.com', team='DC'),
            User.objects.create(name='Superman', email='superman@dc.com', team='DC'),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]

        self.stdout.write('Creating activities...')
        for user in users:
            Activity.objects.create(user_email=user.email, description='Morning run', duration=30)
            Activity.objects.create(user_email=user.email, description='Evening workout', duration=45)

        self.stdout.write('Creating workouts...')
        Workout.objects.create(name='Pushups', reps=20)
        Workout.objects.create(name='Situps', reps=30)
        Workout.objects.create(name='Squats', reps=40)

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        self.stdout.write('Creating unique index on email field for users...')
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
