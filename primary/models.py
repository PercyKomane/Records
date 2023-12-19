from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    wage = models.IntegerField()

    def __str__(self):
        return self.name
    
class Description(models.Model):
    employee_name = models.ForeignKey(Employees, on_delete=models.CASCADE)
    job_description = models.TextField()
    age = models.IntegerField()
    years_working = models.IntegerField()
    
    def __str__(self):
        return self.employee_name
    
class SuperUser(models.Model):
    employee_name = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
    