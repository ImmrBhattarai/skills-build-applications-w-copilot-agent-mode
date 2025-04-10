from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default'].get('PORT', 27017))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(test_users)
        db.teams.insert_many(test_teams)
        db.activities.insert_many(test_activities)
        db.leaderboard.insert_many(test_leaderboard)
        db.workouts.insert_many(test_workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
