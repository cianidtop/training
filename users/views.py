from django.shortcuts import render, redirect
from .forms import Userprofile, UserForms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForms(request.POST)
        profile_form = Userprofile(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # save info in database
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # one to one relatonship
            return redirect('home-main')
    else:
            user_form = UserForms()
            profile_form = Userprofile()
    return render(request, 'users/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

