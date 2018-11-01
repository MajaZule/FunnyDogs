from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('7/', views.second_page, name = 'second_page')
]