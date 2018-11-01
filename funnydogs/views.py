from django.shortcuts import render
from django.http import HttpResponse
from funnydogs.models import Entry


def index(request):
	entries = Entry.objects.all()
	result = ''

	for entry in entries:
		result += str(entry.content) + '<br>'

	return HttpResponse(result)

def second_page(request):
	return HttpResponse('I guess this is the second page.')
