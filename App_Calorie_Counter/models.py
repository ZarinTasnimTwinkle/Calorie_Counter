from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    def __str__(self):
        return self.username

class UserEditModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    age = models.FloatField(null=True,blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    height = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)  
    bmr = models.FloatField(null=True,blank=True)  
    def __str__(self):
        return self.user.username

class FoodEntryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    calories = models.FloatField()