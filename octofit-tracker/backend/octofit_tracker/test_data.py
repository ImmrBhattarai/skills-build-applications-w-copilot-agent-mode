from bson import ObjectId

test_users = [
    {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"_id": ObjectId(), "name": "Team Thunder", "members": ["thundergod", "metalgeek"]},
    {"_id": ObjectId(), "name": "Team Cool", "members": ["zerocool", "crashoverride"]},
]

test_activities = [
    {"_id": ObjectId(), "user": "thundergod", "activity": "Running", "duration": 30},
    {"_id": ObjectId(), "user": "metalgeek", "activity": "Cycling", "duration": 45},
]

test_leaderboard = [
    {"_id": ObjectId(), "team": "Team Thunder", "points": 100},
    {"_id": ObjectId(), "team": "Team Cool", "points": 80},
]

test_workouts = [
    {"_id": ObjectId(), "name": "Morning Run", "duration": 30, "calories_burned": 300},
    {"_id": ObjectId(), "name": "Evening Yoga", "duration": 60, "calories_burned": 200},
]
