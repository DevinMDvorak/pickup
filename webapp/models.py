from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal


# Create your models here.

class UserProfile(models.Model):
    # This extends Djangos default user class
    user = models.OneToOneField(User)
    
    # Extra attributes that are added to the default user
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    # We will need to add some fields such as location, favorite sport, distance willing to travel, etc.
    
    # Override the __unicode__() method to return the username
    def __unicode__(self):
        return self.user.username


class Game(models.Model):

    BASKETBALL = 'Basketball'
    FOOTBALL = 'Football'
    TENNIS = 'Tennis'
    CYCLING = 'Cycling'
    SOCCER = 'Soccer'
    BASEBALL = 'Baseball'
    ULTIMATEFRISBEE = 'Ultimate Frisbee'

    SPORTS = (
        (BASKETBALL, 'Basketball'),
        (FOOTBALL, 'Football'),
        (TENNIS, 'Tennis'),
        (CYCLING, 'Cycling'),
        (SOCCER, 'Soccer'),
        (BASEBALL, 'Baseball'),
        (ULTIMATEFRISBEE, 'Ultimate Frisbee'),
    )
    sport = models.CharField(max_length = 32, choices = SPORTS)
    date = models.DateField((u"Date"), blank=False)
    time = models.TimeField((u"Time"), blank=False)
    description = models.TextField(max_length = 512)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal(0))
    longitude = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal(0))
    address = models.TextField(max_length = 512, default="")

