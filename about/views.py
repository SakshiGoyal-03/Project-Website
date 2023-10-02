from django.shortcuts import render , redirect 
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')

# Create your views here.
def about(request):
    return render(request , 'about.html')
def home(request):
    return render(request , 'about.html')    
