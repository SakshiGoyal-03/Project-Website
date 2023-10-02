from django.shortcuts import render, redirect
from django.http import HttpResponse  # Import HttpResponse from django.http
from django.contrib.auth import authenticate, login, logout
from django. contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')

def home(request):
    return render(request, 'home.html')

def dologout(request):
    logout(request)
    return render(request , 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/')  # Replace 'home' with the URL name of your home page view
        else:
            messages.error(request, 'Invalid login credentials.')
            # return HttpResponse("Invalid login credentials.")

    return render(request, 'login.html')
def help(request):
    return render(request , 'help.html' )