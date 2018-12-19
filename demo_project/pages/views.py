from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

class HomePageView(TemplateView):
	template_name= 'home.html'

def secret(request):
	if request.user.is_authenticated:
		current_user = request.user
		print (current_user.id)
		return redirect('/')
	else:
		return redirect('users/login')