from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
from .models import Todo


def index(request):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:	
		current_user = request.user
		print (current_user)
		# print(type(current_user))
		todos = Todo.objects.filter(user=current_user)
		print(type(todos))
		context = {
			'todos':todos,
			'user':'True'
		}
		return render(request, 'index.html',context)

def details(request,todo_id):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:
		todo = Todo.objects.get(id=todo_id)
		context = {
			'todo':todo,
			'user':'True'
		}
		return render(request,'details.html',context)

def add(request):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:
		if(request.method=='POST'):
			title = request.POST['title']
			text = request.POST['text']
			user = request.user
			todo = Todo(title=title,text=text,user = user)
			todo.save()
			return redirect('/')
		else:
			context = {
				'user':'True'
			}
			return render(request,'add.html',context)

def edit(request,todo_id):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:	
		if(request.method=='POST'):
			title = request.POST['title']
			text = request.POST['text']
			todo = Todo.objects.get(id=todo_id)
			todo.title = title
			todo.text = text
			todo.save()
			return redirect('/')
		else:
			todo = Todo.objects.get(id=todo_id)
			context = {
				'todo':todo,
				'user':'True'
			}
			print(todo)
			return render(request,'edit.html',context)

def delete(request,todo_id):
	if not request.user.is_authenticated:
		return redirect('/loginuser')
	else:
		todo = Todo.objects.get(id=todo_id)
		todo.delete()
		return redirect('/')

def login_view(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(
			request,
			username=username, 
			password=password)
		if user is not None:
			login(request,user)
			print(user)
			return redirect('/')
		else:
			print("PROBLEM")
			context = {
				'message':'Check login credentials'
			}
			return render(request,'login.html',context)
	else:
		return render(request,'login.html')

def logout_view(request):
	logout(request)
	return redirect('/')

def signup_view(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		email 	 = request.POST['email']
		try:
			user = User.objects.create_user(
				username=username,
				email=email,
				password=password)
		except:
			context = {
				'message':'This account can not be created.'
			}
			return render(request,'signup.html',context)
		user.save()
		if user is not None:
			return redirect('/')
		else:
			return redirect('/signupuser')
	else:
		return render(request,'signup.html')