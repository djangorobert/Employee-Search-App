from django.urls import path


from . import views

urlpatterns = [
	
	path('search', views.search, name='search'),
	path('', views.EmployeesList.as_view()),
	path('<int:pk>/', views.EmployeesDetail.as_view()),
]