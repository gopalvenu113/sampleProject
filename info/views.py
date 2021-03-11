from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee
from django.urls import reverse

def my_index(request):
    # return HttpResponse("Welcome to my index page")
    employee_list = Employee.objects.values('id', 'name', 'sal')
    return render(request, 'info/home.html', context={'employee_details': employee_list})


def my_detailed_view(request, emp_id):
    employee = Employee.objects.filter(id=emp_id)
    return render(request, 'info/home.html', context={'employee_details': employee})


# def end_page(request):
#     # return HttpResponse("Thank You for visiting my site")
#     return render(request, 'info/end.html')

def create_form(request):
    return render(request, 'info/create_emp.html')

def update_form_view(request, emp_id):
    employee = Employee.objects.filter(id=emp_id).last()
    return render(request, 'info/update_emp.html', context={'employee_details': employee})

def create_emp(request):
    last_emp_id = Employee.objects.last().id
    name = request.POST.get('name', 'emp_name')
    sal = request.POST.get('sal', 'emp_sal')
    emp = Employee.objects.create(name=name, sal=sal, id=last_emp_id+1)
    return HttpResponseRedirect(reverse('info:my_detailed_view', args=(emp.id,)))


def delete_view(request, emp_id):
    Employee.objects.filter(id=emp_id).delete()
    # return HttpResponseRedirect(reverse('info:my_index_view'))
    employee_list = Employee.objects.values('id', 'name', 'sal')
    return render(request, 'info/home.html', context={'employee_details': employee_list})

def update_view(request, emp_id):
    emp = Employee.objects.filter(id=emp_id).last()
    name = request.POST.get('name', emp.name)
    sal = request.POST.get('sal', emp.sal)
    emp.name = name
    emp.sal = sal
    emp.save()
    return HttpResponseRedirect(reverse('info:my_detailed_view', args=(emp.id,)))