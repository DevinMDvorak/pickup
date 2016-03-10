from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile, Game
from django.forms import widgets

# Overrides all time field inputs so that when the form
# is sent to the host the field will be of type='time'
forms.TimeInput.input_type="time"

# Overrides all date field inputs so that when the form
# is sent to the host the field will be of type='date'
forms.DateInput.input_type="date"

# Form built for the default Django User class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


# This form will need to be updated with additional fields
# once the UserProfile model has been updated
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class NewGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('sport', 'date', 'time', 'description', 'latitude', 'longitude', 'address')