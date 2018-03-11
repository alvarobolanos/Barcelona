from django.shortcuts import render
from .models import Agent

# Create your views here.

def index(request):
    agents = Agent.objects.all()
    return render(request, 'index.html', {'agents':agents})