from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you would typically save this data to your database
        # or send an email. For now, we'll just redirect back to the home page.
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))