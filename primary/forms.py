from django.forms import ModelForm
from .models import Employees, SuperUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

class SuperUserForm(ModelForm):
    class Meta:
        model = SuperUser
        fields = '__all__'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class SuperUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = SuperUser
        fields = ['password']