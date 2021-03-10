from django.db import models

# Create your models here.



class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    sal = models.DecimalField(null=True, decimal_places=2, max_digits=10)

    # def __init__(self):
    #     return

    def __str__(self):
        return self.name
