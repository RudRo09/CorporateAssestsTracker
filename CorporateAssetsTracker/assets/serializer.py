from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog


# CompanySerializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# EmployeeSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# DeviceSerializer
class DeviceSerializer(serializers.ModelSerializer):
    assigned_to = EmployeeSerializer(read_only=True)

    class Meta:
        model = Device
        fields = '__all__'


#DeviceLogSerializer
class DeviceLogSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = DeviceLog
        fields = '__all__'
