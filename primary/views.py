from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employees, Description, SuperUser
from .forms import EmployeesForm

def home(request):
    details = Employees.objects.all()

    context = {'details': details}
    return render(request, 'primary/home.html', context)

def newEmployee(request):

    if request.method == 'POST':

        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        # firstName = request.POST.get('firstName')
        # lastName = request.POST.get('lastName')
    
    else:
        form = EmployeesForm()
    
    context = {'form': form}
    return render(request, 'primary/newEmployee.html', context)

def employeeDetails(request, pk):
    details = Employees.objects.get(id=pk)

    context = {'details': details}
    return render(request, 'primary/employeeDetails.html', context)

def deleteRecord(request, pk):
    details = Employees.objects.get(id=pk)

    if request.method == 'POST':
        details.delete()
        return redirect('home')
    
    context = {'details': details}
    return render(request, 'primary/delete.html', context)

    


