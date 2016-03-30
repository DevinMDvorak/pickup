from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from webapp.forms import UserForm, UserProfileForm, NewGameForm, GroupProfileForm, JoinGameForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from decimal import Decimal
from webapp.models import Game, UserProfile, User
import json
from django.core import serializers

# Create your views here

# Homepage, this view will pass all local games from database
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    game_list = serializers.serialize('json', Game.objects.all())
    username = request.user
    userprofiles = serializers.serialize('json', User.objects.all())
    if request.method == 'POST':
        try:
            gameName = request.POST['game']
            print gameName
            allGames = Game.objects.all()
            for n in allGames:
                if n.__unicode__() == gameName:
                    n.joinees.add(User.objects.get(username = str(request.user)))
                    print str(request.user) + " added to game!"
                print n.__unicode__()
        except KeyError:
            print "Where is game??"
    else:
        print "request.method was not equal to post"
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    return render(request, 'webapp/index.html', {'game_list': game_list, 'username': username, 'userprofiles': userprofiles})


def register(request):
    
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        # If the two forms are valid...
        if user_form.is_valid(): #and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #profile.picture = request.FILES['picture']
        
            # Now we save the UserProfile model instance.
            #profile.save()
    
            # Update our variable to tell the template registration was successful.
            registered = True
        
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
    profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'webapp/register.html',
                  {'user_form': user_form, 'registered': registered} )





def user_login(request):
    
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/webapp/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your PickUp account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'webapp/login.html', {})



# We use the login_required() decorator to ensure only those logged in can access the view.
# Make sure to use this on every view that requires the user to be logged in
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    
    # Take the user back to the homepage.
    return HttpResponseRedirect('/webapp/')

@login_required
def creategame(request):
    if request.method == "POST":
        form = NewGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.owner = UserProfile.objects.get(user__username = str(request.user))
            game.ownerName = str(request.user)
            game.published_date = timezone.now()
            game.save()
            game.joinees.add(User.objects.get(username = str(request.user)))
            game.save()
            return redirect('/webapp/')
    else:
        form = NewGameForm()
    return render(request, 'webapp/newgame.html', {'form': form})

@login_required
def profile_view(request, username):
    if username == str(request.user):
        editable = 1
    else:
        editable = 0
    print request.user
    print username
    account = UserProfile.objects.get(user__username = username)
    image = account.picture
    name = account.user.username
    friends = account.friends
    return render(request, 'webapp/profile_view.html', {'image': image, 'editable': editable, 'name': name, 'friends': friends,})


@login_required
def groups(request):
	if request.method == 'POST':
		group_form = GroupProfileForm(request.POST)
		if group_form.is_valid():
			group = group_forms.save(commit=False)
			group.published_date = timezone.now()
			group.save()
			return redirect('/webapp/')
		else:
			group_form = GroupProfileForm()
	return render(request, 'webapp/groups.html')


@login_required
def groups_list(request):
	groups_list = GroupProfile.objects.all()
	output = ', '.join([a.name for a in groups_list])
	return render(request, 'webapp/groupslist.html', {'output': output})


@login_required	
def group(request, group_id):
	return HttpResponse("You're viewing group %s." % group_id)
