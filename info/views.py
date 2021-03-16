from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from info.serializers import EmployeeSerializer
from rest_framework.decorators import action
from django.db.models import Max

def my_index(request):
    # return HttpResponse("Welcome to my index page")
    employee_list = Employee.objects.values('id', 'name', 'sal')
    # return render(request, 'info/home.html', context={'employee_details': employee_list})
    return HttpResponse(employee_list)


def my_detailed_view(request, emp_id):
    try:
        employee = Employee.objects.filter(id=emp_id)
        if employee.exists():
            return render(request, 'info/home.html', context={'employee_details': employee})
        raise Exception("Employee not found in the database")
    except Exception as e:
        return render(request, 'info/info.html', context={'info': str(e)})


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
    return HttpResponseRedirect(reverse('info:my_index_view'))
    # employee_list = Employee.objects.values('id', 'name', 'sal')
    # return render(request, 'info/home.html', context={'employee_details': employee_list})

def update_view(request, emp_id):
    emp = Employee.objects.filter(id=emp_id).last()
    name = request.POST.get('name', emp.name)
    sal = request.POST.get('sal', emp.sal)
    Employee.objects.filter(id=emp_id).update(name=name, sal=sal)
    # emp.name = name
    # emp.sal = sal
    # emp.save()
    return HttpResponseRedirect(reverse('info:my_detailed_view', args=(emp.id,)))



class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    allowed_methods = ['get', 'post', 'patch', 'delete']


    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        max_sal = Employee.objects.aggregate(Max('sal'))
        max_sal = max_sal['sal__max']
        context = {'max_sal': max_sal}
        serializer = self.get_serializer(queryset, many=True, context=context)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        queryset = self.get_object()
        serializer = self.get_serializer(instance=queryset, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = self.queryset.filter(id=pk).delete()
        return Response({'detail': 'Object deleted succesfully'})
    
    @action(methods=['get'], detail=False, url_name='increase_sal')
    def increase_sal(self, request, *args, **kwargs):
        queryset = self.queryset
        for obj in queryset:
            obj.sal = 1.1 * float(obj.sal)
            obj.save(update_fields=['sal'])
        queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
