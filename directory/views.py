from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})


def detail(request, slug):
    employee = Employee.objects.get(slug=slug)
    return render(request, 'detail.html', {'employee': employee})


def edit(request, slug):
    employee = Employee.objects.get(slug=slug)
    if (request.method == 'POST'):
        form = EmployeeForm(data=request.POST, instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('detail', args=[slug]))
    else:
        employee_dict = model_to_dict(employee)
        form = EmployeeForm(employee_dict)
        return render(request, 'edit.html', {'form':form})