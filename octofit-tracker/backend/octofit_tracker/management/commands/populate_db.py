from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import sys
import os

# Dynamically add the octofit_tracker directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts


class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        users = {}
        for user_data in test_users:
            user = User.objects.create(email=user_data['email'], name=user_data['name'])
            users[user_data['email']] = user

        # Create Teams
        teams = {}
        for team_data in test_teams:
            team = Team.objects.create(name=team_data['name'], description=team_data['description'])
            teams[team_data['name']] = team

        # Create Activities
        activities = {}
        for activity_data in test_activities:
            activity = Activity.objects.create(name=activity_data['name'], duration=activity_data['duration'])
            activities[activity_data['name']] = activity

        # Create Leaderboard Entries
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.create(user=users[leaderboard_data['user_email']], score=leaderboard_data['score'])

        # Create Workouts
        for workout_data in test_workouts:
            Workout.objects.create(user=users[workout_data['user_email']], activity=activities[workout_data['activity_name']], date=workout_data['date'])

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
