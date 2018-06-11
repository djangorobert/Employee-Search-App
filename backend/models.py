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
		
		
	