from django.shortcuts import render
from django.views.generic import DetailView, ListView

from events.models import Event
from datetime import datetime

class EventView(DetailView):

	model = Event
	template_name = "event_details.html"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		if not kwargs.get('pk') or not kwargs.get('slug', '').strip():
			return redirect(self.object, permanent=True)
		
		return super(EventView, self).get(request, *args, **kwargs)

class EventListView(ListView):

	queryset=Event.objects.all()
	template_name = "event_list.html"

	def get_context_data(self, **kwargs):
		events = Event.objects.order_by('start_date').filter(is_published=True, end_date__gte=datetime.now())

		context = super(EventListView, self).get_context_data(**kwargs)
		if events:
			context['events'] = events
		else:
			context['events'] = ""
		return context