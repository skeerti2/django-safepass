from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from password_list.models import User


# Create your views here.

def displayLanding(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, "landing.html", context)

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, "register.html", context)

def signup(request):
    if request.method == "POST":
        #pass form data to a new instance of user
        #returns a new instance of form that is valid/invalid
        form = UserCreationForm(request.POST)
        print("came to sign up")
        print(form.errors)
        if form.is_valid():
            print("form is valid")
            #saves user data to db
            user = form.save()
            auth_login(request, user)
            print(user)
            user = User.objects.create(username=request.user.username)
            user.save()
            #need to log user in
            return redirect(reverse('password_list:postLoginLanding'))
    #context = {'form': form}
    #return render(request, "signup.html", context)


def login(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(reverse('password_list:postLoginLanding'))
    else:
        form = AuthenticationForm()
    return render(request, "landing.html", {'form': form})
