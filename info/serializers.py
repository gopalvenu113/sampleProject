from rest_framework import serializers
from info.models import Employee
from django.db.models import Max

class EmployeeSerializer(serializers.ModelSerializer):
    per_sal = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'sal', 'per_sal']
    
    def get_per_sal(self, instance):
        sal = instance.sal
        context = self.context
        max_sal = context['max_sal']
        return (sal / max_sal) * 100