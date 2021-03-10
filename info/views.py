from django.shortcuts import render

from django.http import HttpResponse
from .models import Employee

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