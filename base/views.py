from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'base/index.html')
    

def signUp(request):
	""" User registratiom page """
	
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserRegistrationForm()
	context = {'form' : form}
	return render (request, "base/signUp.html", context)


def signIn(request):
    if request.method == "POST":
	    form = UserLoginForm(request, request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    
		    user = authenticate(username=username, password=password)
		    
		    if user is not None:
			    login(request, user)
			    messages.info(request, f"You are now logged in as {username}.")
			    return redirect("index")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = UserLoginForm()
    context= {'form' : form}
    return render(request, "base/signin.html", context)


def signOut(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")


@login_required
def UserDashBoard(request):
    UserName = request.user.first_name
    context = {'UserName' : UserName}
    return render(request, 'base/UserDashBoard.html',context)


@login_required
def createMeeting(request):
    UserFirstName = request.user.first_name
    UserLastName = request.user.last_name
    UserFullName = UserFirstName + " " + UserLastName

    context = {'UserFullName' : UserFullName}
    return render(request, 'base/visagelogs.html', context)


@login_required
def joinMeeting(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/createMeeting?roomID=" + roomID)
    return render(request, 'base/joinMeeting.html')

