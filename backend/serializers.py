from rest_framework import serializers
from .models import Employees

		
class EmployeesSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		
		model = Employees