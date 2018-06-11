from .models import Employees

import django_filters


		

		
class EmployeesFilter(django_filters.FilterSet):
	
	
	class Meta:
		model = Employees
		fields = {
		'first_name': ['exact'],
		'last_name': ['exact'],
		'hired': ['year', 'year__gt', 'year__lt', ],
		'group': ['exact'],
		'gender': ['exact'],
		}