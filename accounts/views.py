from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):

	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, "Invalid Credentials")
			return redirect('login')

	else:
		return render(request, 'login.html')


def register(request):

	if request.method == 'POST':

		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']
		
		
		if pass1 == pass2:

			if User.objects.filter(username=username).exists():

				print("username is taken")
				messages.info(request, "username is taken")
				return redirect('register')

			elif User.objects.filter(email= email).exists():

				print("email already used")
				messages.info(request, "Email already used")

			else:

				user = User.objects.create_user(username=username, password=pass1, email=email, first_name=firstname, last_name=lastname )
				user.save();

				print("Account Created successfully")
				messages.info(request, "Account Created successfully")
				return redirect('login')
		else:
			print("password not matching..!")
			messages.info(request, "Password not matching.. Retry.. !")
			return redirect('register')

	else:
		return render(request,'register.html')

def logout(request):
	auth.logout(request)
	return redirect('/')