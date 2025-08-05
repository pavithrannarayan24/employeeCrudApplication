from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .form import Employeeforms

# List all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'students/employee_list.html', {'employees': employees})

# Create a new employee
def employee_create(request):
    form = Employeeforms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'students/employee_form.html', {'form': form})

# Update an existing employee
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = Employeeforms(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'students/employee_form.html', {'form': form})

# Delete an employee
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'students/employee_confirm_delete.html', {'employee': employee})


# Create your views here.
