from django.shortcuts import render
from django.http import HttpResponse
from funnydogs.models import Entry
from django.template import loader
from .models import Entry


def index(request):
	latest_entries_list = Entry.objects.all().order_by('-time_stamp')[:10]
	template = loader.get_template('funnydogs/index.html')
	result = {
		'latest_entries_list':latest_entries_list,
	}

	return HttpResponse(template.render(result, request))

def entry(request, entry_id):
	try:
		entry = Entry.objects.get(pk=entry_id)
	except Entry.DoesNotExist:
		raise Http404('This entry does not exist.')
	return render(request, 'funnydogs/entry.html', {'entry': entry})

def create_entry(request):
	return HttpResponse('Page where user creates new entries.')

def personal_page(request):
	return HttpResponse('Personal user page, where user can edit profile, browse entries, etc.')

