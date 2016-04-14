from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal
import uuid


# Create your models here.

class UserProfile(models.Model):
    # This extends Djangos default user class
    user = models.OneToOneField(User)
    
    # Extra attributes that are added to the default user
    picture = models.ImageField(upload_to='profile_images', default='static/images/defaultpic.png')
    friends = models.ManyToManyField("self", blank=True)
    bio = models.TextField(max_length = 512, default="")
    
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
    owner = models.ForeignKey(UserProfile, related_name="profiles")
    ownerName = models.CharField(max_length = 30)
    joinees = models.ManyToManyField(User, blank=True)
    sport = models.CharField(max_length = 32, choices = SPORTS)
    date = models.DateField((u"Date"), blank=False)
    time = models.TimeField((u"Time"), blank=False)
    description = models.TextField(max_length = 512)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(max_length = 512, default="")

    def as_json(self):
        return dict(
            owner = self.owner,
            sport = self.sport,
            date = self.date.isoformat(),
            time = self.time.isoformat(),
            description = self.description,
            latitude = self.latitude,
            longitude = self.longitude,
            address = self.address
        )

    def __unicode__(self):
        return self.owner.user.username + " " + self.sport + " " + str(self.date)


class GroupProfile(models.Model):
	name = models.CharField(max_length=50)
	creator = models.CharField(max_length=50)
	sport = models.CharField(max_length=50)
	zipcode = models.IntegerField()

	def __unicode__(self):
        # This should be self.name
		return self.name + " - " + self.creator
