from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewset)



urlpatterns = [
    path('', include(router.urls)),
    path('home', views.my_index, name='my_index_view'),
    path('home/<int:emp_id>', views.my_detailed_view, name='my_detailed_view'),
    path('home/delete/<int:emp_id>', views.delete_view, name='delete_view'),
    path('update_view/<int:emp_id>', views.update_view, name='update_view'),
    path('home/update_form/<int:emp_id>', views.update_form_view, name='update_form_view'),
    path('create_form', views.create_form, name='create_employee_form'),
    path('create_emp', views.create_emp, name='create_emp'),
    # path('end', views.end_page, name='end_page')
]
