from django.shortcuts import render
from .models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees':employees})

def detail(request, slug):
    employee = Employee.objects.get(slug=slug)
    return render(request, 'detail.html', {'employee':employee})