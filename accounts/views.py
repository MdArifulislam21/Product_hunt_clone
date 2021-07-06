from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import auth


def signup(request):
	if request.method =="POST":
		# The user wants an accounts
		first_name = request.POST.get('f_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password1 == password2:
		    if User.objects.filter(username=username).exists() :
		    
		        return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})

		    elif User.objects.filter(email=email).exists() :
		        return render(request, 'accounts/signup.html', {'error': 'email has already been taken'})

		    else:
		        user = User.objects.create_user(username= username, password= password1, email=email, first_name=first_name, last_name=last_name)
		        user.save()
		        print('user created')
		        auth.login(request, user)
		        return redirect('home')
	else:
		# The user wants to enter info
		return render(request, 'accounts/signup.html')


def login(request):
	if request.method == "POST":
		user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error': "Username or Password didn't match."})
	else:
		return render(request, 'accounts/login.html')


def logout(request):

	auth.logout(request)
	return redirect('home')