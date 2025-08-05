from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Stream = models.CharField(max_length=100)
    email = models.EmailField(default=None)
    designation = models.CharField(max_length=100,default='Employee')
    salary = models.DecimalField(max_digits=10, decimal_places=2,default=30000.00)

    def __str__(self):
        return self.name
# Create your models here.
