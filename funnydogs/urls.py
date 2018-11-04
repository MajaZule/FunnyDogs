from django.urls import path

from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('<int:pk>/', views.EntryView.as_view(), name = 'entry'),
	path('create/', views.create_entry, name = 'create_entry'),
	path('personal/', views.personal_page, name = 'personal_page'),
]