from django.shortcuts import render, redirect
from ratings.models import Ratings
from ratings.forms import NewRatingForm

def read(request):
	if request.method == "GET":
		objects = Ratings.objects.all() 
		return render(request, "ratings.html", {'res' : objects})	

def create(request):
	if request.method == "POST":
		newRatingForm = NewRatingForm(request.POST or None)
		
		if newRatingForm.is_valid():
			newRatingForm.save()

		return redirect('/ratings/read')

def update(request, dest):
	if request.method == "POST":
		t = Ratings.objects.get(destination=dest)
		t.rating = request.POST.get('rating', '')
		t.save()

		return redirect('/ratings/read')

def readOne(request, dest):
	if request.method == "GET":
		object = Ratings.objects.get(destination=dest) 
		return render(request, "ratings.html", {'res' : [ object ] })	

def delete(request, dest):
	Ratings.objects.filter(destination=dest).delete() 
	return redirect('/ratings/read')
