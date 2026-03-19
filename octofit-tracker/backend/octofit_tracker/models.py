from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)  # Store team name as reference
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_email = models.EmailField()  # Store user email as reference
    description = models.CharField(max_length=255)
    duration = models.IntegerField()  # duration in minutes
    def __str__(self):
        return f"{self.user_email} - {self.description}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    reps = models.IntegerField()
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.CharField(max_length=100)  # Store team name as reference
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.points}"
