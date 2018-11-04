from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from funnydogs.models import Entry
from django.template import loader
from .models import Entry
from django.views import generic
from django.urls import reverse

from .models import Entry


class IndexView(generic.ListView):
	template_name = 'funnydogs/index.html'
	context_object_name = 'latest_entries_list'
	
	def get_queryset(self):
		return Entry.objects.order_by('-time_stamp')[:10]

class EntryView(generic.DetailView):
	model = Entry
	template_name = 'funnydogs/entry.html'

def create_entry(request):
	return HttpResponse('Page where user creates new entries.')

def personal_page(request):
	return HttpResponse('Personal user page, where user can edit profile, browse entries, etc.')

