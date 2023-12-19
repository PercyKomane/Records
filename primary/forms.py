from django.forms import ModelForm
from .models import Employees

class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'