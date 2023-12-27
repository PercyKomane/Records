from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employees, Description, SuperUser
from .forms import EmployeesForm, LoginForm, RegistrationForm, SuperUserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q

def loginPage(request):
    details = SuperUser.objects.all()

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']

            try:
                superuser = SuperUser.objects.get(employee_name__username=username)
            except SuperUser.DoesNotExist:
                messages.error(request, "User does not exist")
                return render(request, 'primary/loginPage.html', {'details': details})

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password does not exist')
    else:
        form = LoginForm()

    context = {'details': details, 'form': form}
    return render(request, 'primary/loginPage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        superuser_form = SuperUserRegistrationForm(request.POST)

        if user_form.is_valid() and superuser_form.is_valid():
            user = user_form.save()
            password = superuser_form.cleaned_data['password']
            superuser = SuperUser(employee_name=user, password=password)
            superuser.save()

            login(request, user)
            return redirect('home')
    else:
        user_form = RegistrationForm()
        superuser_form = SuperUserRegistrationForm()

    context = {'user_form': user_form, 'superuser_form': superuser_form}
    return render(request, 'primary/registerPage.html', context)

def home(request):
    details = Employees.objects.all()

    context = {'details': details}
    return render(request, 'primary/home.html', context)

@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
def updateEmployee(request, pk):
    # Retrieve the employee details from the database
    employee = get_object_or_404(Employees, id=pk)

    if request.method == 'POST':
        # Populate the form with the current data from the database
        form = EmployeesForm(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('employeeDetails', pk=pk)
    else:
        # Populate the form with the current data from the database
        form = EmployeesForm(instance=employee)

    context = {'form': form, 'employee': employee}
    return render(request, 'primary/updateEmployee.html', context)

@login_required(login_url='loginPage')
def employeeDetails(request, pk):
    details = Employees.objects.get(id=pk)

    context = {'details': details}
    return render(request, 'primary/employeeDetails.html', context)

@login_required(login_url='loginPage')
def deleteRecord(request, pk):
    details = Employees.objects.get(id=pk)

    if request.method == 'POST':
        details.delete()
        return redirect('home')
    
    context = {'details': details}
    return render(request, 'primary/delete.html', context)

@login_required(login_url='loginPage')
def searchEmployee(request):
    query = request.GET.get('q')

    if query:
        # Perform a case-insensitive search for employees
        results = Employees.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        results = Employees.objects.none()

    context = {'results': results, 'query': query}
    return render(request, 'primary/home.html', context)