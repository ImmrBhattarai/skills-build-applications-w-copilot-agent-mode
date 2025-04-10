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
            team = Team.objects.create(name=team_data['name'])
            teams[team_data['name']] = team

        # Create Activities
        for activity_data in test_activities:
            Activity.objects.create(
                user=users[activity_data['user_email']],
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration'],
                calories_burned=activity_data['calories_burned'],
                date=activity_data['date']
            )

        # Create Leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.create(
                team=teams[leaderboard_data['team_name']],
                points=leaderboard_data['points']
            )

        # Create Workouts
        for workout_data in test_workouts:
            Workout.objects.create(
                name=workout_data['name'],
                duration=workout_data['duration'],
                calories_burned=workout_data['calories_burned']
            )

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
