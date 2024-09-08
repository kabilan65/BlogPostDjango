from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        get_by_username = User.objects.filter(username=username)
        if get_by_username:
            messages.warning(request, "Username Already Exists!")
            return redirect('user_register')
        if password1 != password2:
            messages.warning(request, "Password Doesn't Matches")
            return redirect('user_register')
        elif len(password1) < 8:
            messages.warning(request, "Password Should Be Atlease 8 Characters")
            return redirect('user_register')
        
        new_user = User.objects.create_user(username=username, email=email, password=password1)
        new_user.save()
        messages.success(request, 'Account Created Successfully!')
        return redirect('user_login')

    return render(request, 'auth/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        valid_user = authenticate(username=username, password=password)
        if valid_user:
            login(request, valid_user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('user_login')