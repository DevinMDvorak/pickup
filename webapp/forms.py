from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile


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