from django.db import models
from django.utils import timezone   # to ensure that dates and times are accurate and consistent across different timezones.


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.company_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.employee_name


class Device(models.Model):
    device_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=255)
    
    def __str__(self):
        return self.device_name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(default=timezone.now)
    check_in_date = models.DateTimeField(null=True, blank=True)
    check_out_condition = models.CharField(max_length=255)
    check_in_condition = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f'{self.device} - {self.employee}'