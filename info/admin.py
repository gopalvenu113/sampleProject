from django.contrib import admin
from .models import Employee
# Register your models here.
from prettyjson import PrettyJSONWidget

class EmployeeAdmin(admin.ModelAdmin):
    model=Employee
    list_display=('id', 'name', 'sal')
    list_filter=('name',)
    search_fields=('name',)


admin.site.register(Employee, EmployeeAdmin)