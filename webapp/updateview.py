from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from webapp.forms import UserForm, UserProfileForm, NewGameForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)