from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
	return render(request, "pokes/index.html")

def register(request):
	if request.method == "POST":
		regVal = User.objects.registerUser(request.POST["name"], request.POST["alias"], request.POST["email"], request.POST["password"], request.POST["confirmpass"])
		request.session["name"] = request.POST["name"]
		if not regVal:		
			User.objects.create(name=request.POST["name"], alias=request.POST["alias"], email=request.POST["email"], password=request.POST["password"], confirmpass=request.POST["confirmpass"])
			return redirect("/pokes")
		else:
			for error in regVal:
				messages.error(request, error)
			return redirect("/")

def login(request):
	if request.method == "POST":
		print "login"
		user = User.objects.loginUser(request.POST["logemail"], request.POST["logpassword"])
		if user:
			print "pokes"
			return redirect("/pokes")
		else:
			print "come back"
			messages.error(request, "Email or password incorrect")
			return redirect("/")

def pokehist(request):
	if request.POST["poke"] == "oliver":
		request.session["oliver"] = 1 + request.session["oliver"]

	if request.POST["poke"] == "diane":
		request.session["diane"] = 1 + request.session["diane"]

	if request.POST["poke"] == "jerry":
		request.session["jerry"] = 1 + request.session["jerry"]

	if request.POST["poke"] == "john":
		request.session["john"] = 1 + request.session["john"]

	if request.POST["poke"] == "olivia":
		request.session["olivia"] = 1 + request.session["olivia"]

	return render(request, "pokes/pokes.html")

def pokes(request):
	context = {
		"poke": User.objects.all()
	}
	return render(request, "pokes/pokes.html", context)




