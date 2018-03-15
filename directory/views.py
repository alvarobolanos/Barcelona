from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees':employees})

def detail(request, slug):
    employee = Employee.objects.get(slug=slug)
    return render(request, 'detail.html', {'employee':employee})

def edit(request, slug):
    form = EmployeeForm()
    return render(request, 'edit.html', {'form':form})