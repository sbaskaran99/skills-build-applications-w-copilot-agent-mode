
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections using PyMongo for a clean slate
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db['octofit_tracker_team'].drop()
        db['octofit_tracker_user'].drop()
        db['octofit_tracker_activity'].drop()
        db['octofit_tracker_workout'].drop()
        db['octofit_tracker_leaderboard'].drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Medium'),
            Workout.objects.create(name='Strength Training', description='Build muscle', difficulty='Hard'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=date.today())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
