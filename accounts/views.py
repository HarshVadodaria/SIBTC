from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.views import View
from django.http import HttpResponse

# Create your views here.

def signup(request):
	if request.method=="POST":
		print("hello")
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	else:
		form=UserCreationForm()

	return render(request,'signup.html',{'form':form})

