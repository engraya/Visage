from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'base/index.html')

def signUp(request):
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
	    form = AuthenticationForm(request, request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    messages.info(request, f"You are now logged in as {username}.")
			    return redirect("main:homepage")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def signOut(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")


def UserDashBoard(request):
    UserName = request.user.first_name
    context = {'UserName' : UserName}
    return render(request, 'base/UserDashBoard.html',context)


def createMeeting(request):
    UserFirstName = request.user.first_name
    UserLastName = request.user.last_name
    UserFullName = UserFirstName + " " + UserLastName

    context = {'UserFullName' : UserFullName}
    return render(request, 'base/visagelogs.html', context)

def joinMeeting(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/createMeeting?roomID=" + roomID)
    return render(request, 'base/joinMeeting.html')