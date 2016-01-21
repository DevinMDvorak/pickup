from django.db import models
from django.contrib.auth.models import User



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