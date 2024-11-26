from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    fitness_goal = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.user.username

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=200)
    duration_minutes = models.IntegerField()
    created_at = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan_name

