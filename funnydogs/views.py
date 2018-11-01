from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse('Nessie is cute.')

def second_page(request):
	return HttpResponse('I guess this is the second page.')
