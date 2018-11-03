from django.shortcuts import render
from django.http import HttpResponse
from funnydogs.models import Entry


def index(request):
	entries = Entry.objects.all().order_by('-time_stamp')[:10]
	result = ''

	for entry in entries:
		result += str(entry.content) + '<br>'

	return HttpResponse(result)

def entry(request, entry_id):
	pass

def create_entry(request):
	return HttpResponse('Page where user creates new entries.')

def personal_page(request):
	return HttpResponse('Personal user page, where user can edit profile, browse entries, etc.')

