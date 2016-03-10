from django import forms
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class HtmlTimeInput(forms.TimeInput):
    input_type = 'time'

