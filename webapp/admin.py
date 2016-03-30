from django.contrib import admin
from webapp.models import UserProfile, Game, GroupProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(GroupProfile)