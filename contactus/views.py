from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.now()
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=date)
        contact.save()
        messages.success(request , "Your message has been sent")
    return render(request, 'contact.html')
