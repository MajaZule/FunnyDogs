from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:entry_id>/', views.entry, name = 'entry'),
	path('create/', views.create_entry, name = 'create_entry'),
	path('personal/', views.personal_page, name = 'personal_page'),
]