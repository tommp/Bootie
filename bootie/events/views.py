from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django import forms
from django.views.generic.edit import FormView
from paddleusers.models import PaddleUser

from events.models import Event, EventRegistrar
from events.forms import EventRegisterForm
from datetime import datetime

class EventRegisterView(FormView):
	template_name = 'event_register.html'
	form_class = EventRegisterForm

	success_url = "/events"

	def form_valid(self, form):
		form.paddle_user = PaddleUser.objects.get(user=self.request.user)
		return super(EventRegisterView, self).form_valid(form)

class EventView(DetailView):

	model = Event
	template_name = "event_details.html"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		if not kwargs.get('pk') or not kwargs.get('slug', '').strip():
			return redirect(self.object, permanent=True)
		
		return super(EventView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(EventView, self).get_context_data(**kwargs)
		context['form'] = EventRegisterForm
		return context


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

class AttendeesView(DetailView):

	model = Event
	template_name = "event_attendees.html"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		if not kwargs.get('pk') or not kwargs.get('slug', '').strip():
			return redirect(self.object, permanent=True)
		
		return super(AttendeesView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(AttendeesView, self).get_context_data(**kwargs)
		return context