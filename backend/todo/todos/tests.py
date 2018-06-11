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