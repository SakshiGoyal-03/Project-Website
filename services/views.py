from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')


# Create your views here.
def service(request):
    return render(request , 'service.html')

# Create your views here.
