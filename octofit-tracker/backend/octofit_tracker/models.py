from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # Replace ObjectIdField with AutoField
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    id = models.AutoField(primary_key=True)  # Replace ObjectIdField with AutoField
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)  # Replace ArrayField with ManyToManyField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Replace ObjectIdField with AutoField for compatibility with SQLite
class Activity(models.Model):
    id = models.AutoField(primary_key=True)  # Replace ObjectIdField with AutoField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.email}"

# Replace ObjectIdField with AutoField for compatibility with SQLite
class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True)  # Replace ObjectIdField with AutoField
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

# Replace ObjectIdField with AutoField for compatibility with SQLite
class Workout(models.Model):
    id = models.AutoField(primary_key=True)  # Replace ObjectIdField with AutoField
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()

    def __str__(self):
        return self.name
