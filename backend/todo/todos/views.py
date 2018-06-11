from rest_framework import generics
from django.shortcuts import render

from .models import Employees
from .serializers import EmployeesSerializer

#Django Filters Imports here
from .filters import EmployeesFilter

#API VIEWS	
class EmployeesList(generics.ListCreateAPIView):
	queryset = Employees.objects.all()
	serializer_class = EmployeesSerializer

	
class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Employees.objects.all()
	serializer_class = EmployeesSerializer
	
	
#This view is for the FRONTEND	
#Create a View for our Search Filters
def search(request):
	
	#Lets use the Employees Model and API so we can then search in our frontend
	emp_list = Employees.objects.all()
	emp_filter = EmployeesFilter(request.GET, queryset=emp_list)
	return render(request, 'todos/todo_list.html', {
													'grab': emp_filter})