# Employee-Search-App
A Basic Search filter in this case is used to Filter through Employees

To Get Started lets build a Virtual Enviorment for this Project I used Pythons web framework Django
I Used python 3.6 and remember python released PIPENV which makes it simpler for us to create a virtualenv and does our requirements.txt 
file for us meaning it has all the dependencies in the PIPENV file so that others can reuse or see what we used to build.

#First Command make sure you have pip and python installed. If you do you can download pipenv with pip.
pip install --user pipenv

#next Lets create a Directory "Aliens" 
mkdir Aliens

# Next CD into your new directory
cd Aliens

#Lets Install the Packages we will need to do this Employee Search APP
pipenv install django

#wait for that to finish then do 
pipenv install djangorestframework

#next install
pipenv install django-filter

#Thats it for this project.

#Lets create a Django Project
#Run this command to start
django-admin startproject Employee

#cd into the new project
cd Employee

#Great!
#Now lets create our app 
#Run this command
python manage.py startapp Employee

#next lets cd into it
cd Employee

#One other thing we will want to create a super user so we can access the Free Admin that django comes with.
python manage.py createsuperuser

# it will prompt you for a username and password pick something you can remember.

#Great
#NExt lets go to settings.py file remember we created the APP Employee we will need to put it under installed apps for it
#to work



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'Employee',
	


]
#Great hit save

# Now we can do a sanity check to make sure that the webserver starts up 
#Run this command

python manage.py runserver

#Go to localhost:8000 that is the default to see your app it should work 

#Ok great now hit ctrl c to stop the server we need to build our Model in this project we are basing it off of an employee
# An Employee will have a first_name, last_name, hire date, gender, Role as in if there a manager or associate.

#Go to models.py and enter this

from django.db import models

# Create your models here.		
class Employees(models.Model):

	
	MALE = 'M'
	FEMALE = 'F'
	GENDER = ( 
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)
	
	MANAGER = 'Manager'
	ASSOCIATE = 'Associate'
	GROUP = ( 
		(MANAGER, 'Manager'),
		(ASSOCIATE, 'Associate'),
	)
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	hired = models.DateTimeField(auto_now=True, null=True)
	gender = models.CharField(
		max_length=2,
		choices=GENDER,
		null=True)
	group = models.CharField(
		max_length=10,
		choices=GROUP,
		null=True)
	

	
	def __str__(self):
		return self.first_name
    
    
#Hit Save
#Great

#Now in the command line run this command to commit the changes through python
python manage.py makemigrations
python manage.py migrate

#That issues the changes to the server

#Next we will create our filters.py file in here is were all the Search funtionality comes from
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
    
#Really simple and basic and gets the job done without going bald lol

#Now for the FRONTEND lets go to our views.py file it should be in your directory under employees
#enter this code.


from django.shortcuts import render

from .models import Employees
#This view is for the FRONTEND	
#Create a View for our Search Filters
def search(request):
	
	#Lets use the Employees Model and API so we can then search in our frontend
	emp_list = Employees.objects.all()
	emp_filter = EmployeesFilter(request.GET, queryset=emp_list)
	return render(request, 'todos/todo_list.html', {
													'grab': emp_filter})
  
#Great now lets create our Template for the user 

#In Django in the APP directory you will create a template folder then under that the name of our app something like this
#employees/templates/employees 
#then in that directory add the html template


<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script></head>

</head>
<body>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="/search">Search</a>
    </div>
    
  </div>
</nav>
<body>
<div class="container">

	<h1>Search : </h1>
	<form method='get'>
		
		{{ grab.form.as_p }}
		
		<button type='submit' class="btn btn-warning"><span class="glyphicon glyphicon-search"></span>Search</span></button>
	
	</form>
</div>


<div class="container">
  
             
  <table class="table table-striped">
    <thead>
      <tr>
		<h2>Results: </h2>
        <th>Firstname</th>
        <th>Lastname</th>
		<th>Year Hired</th>
		<th>Role</th>
		<th>Gender</th>
       
      </tr>
    </thead>
	
    <tbody>
	{% for x in grab.qs %}
      <tr>
	   
        <td>{{ x.first_name }}</td>
        <td>{{ x.last_name }}</td>
		<td>{{ x.hired }}</td>
		<td>{{ x.group }}</td>
		<td>{{ x.gender }}</td>
		
   
      </tr>
	      {% endfor %}  
    </tbody>
  </table>
 
</div>


</body>
</html>  
  
#Great as you will notice I used Bootstrap for the FRONTEND you can go to bootstrap.com and grab the cdn's and add them in your <header>
</header> section.


#We need to update our URLS.py file so that the views can connect to them 
#add this.

from django.urls import path


from . import views

urlpatterns = [
	
	path('search', views.search, name='search'),
  
  
#Great

#One more thing as for TESTING I know it sucks but with django there will be a tests.py file in there we will create a test
#add this to test out our model to see if it works.

from django.test import TestCase

# Create your tests here.
from .models import Employees


class EmployeesCase(TestCase):
	
	def setUp(self):
		Employees.objects.create(first_name='Lance')
		Employees.objects.create(last_name='Jo')
		
	def test_first_name(self):
		f = Employees.objects.get(first_name='Lance')
		expected = f.first_name
		self.assertEqual(expected, 'Lance')
		
	def test_last_name(self):
		last = Employees.objects.get(last_name='Jo')
		expected = last.last_name
		self.assertEqual(expected, 'Jo')
    
    
#Great Now we will go to the command line and run this command
python manage.py tests

# You should see a pass Good JOB!

#Now lets restart our server and see our project 
# YOu may notice that there is no data though :(
#Dont wory go to your admin page localhost:8000/admin
#LOGIN 
#Remember your credentials from when you ran the createsuperuser command ok you will use that to login the admin
# Before we do that lets go to the admin.py file and add this code


from django.contrib import admin

# Register your models here.
from .models import Employees


admin.site.register(Employees)



#Now that your in create some dummie data so that it can populate on our Employee app to test our our Search filter


#Run the command
python manage.py runserver

#Great you did it you now have a Search filter 



