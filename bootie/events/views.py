from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponseForbidden

from paddleusers.models import PaddleUser
from events.models import Event, EventRegistrar
from datetime import datetime

#Too much hacky, reduce hacky, much bad, such ugly, wow
class EventUnRegisterView(DeleteView):
	template_name = 'event_unregister.html'
	model = EventRegistrar

	def get_object(self, queryset=None):
		try:
			registrar = EventRegistrar.objects.get(paddle_user=self.request.user.paddleuser, event_id=self.kwargs['pk'])
			return registrar
		except:
			return ''

	def get_success_url(self):
		event = Event.objects.get(id=self.kwargs['pk'])
		event.number_of_attendees -= 1
		event.save()
		return "/events"

	def delete(self, request, *args, **kwargs):
	    self.object = self.get_object()
	    if self.object and self.object.event.check_if_cancellation_availible():
	    	self.object.delete()
	    else:
	    	return HttpResponseForbidden()
	    return HttpResponseRedirect(self.get_success_url())

class EventRegisterView(CreateView):
	template_name = 'event_register.html'
	model = EventRegistrar
	fields = ("car_seats",)

	success_url = "/events"

	def form_valid(self, form):
		event = Event.objects.get(id=self.kwargs['pk'])
		try:
			registering_user = PaddleUser.objects.get(user=self.request.user)
		except:
			return HttpResponseNotFound("You are trying to register from an invalid account (not a paddleuser) contact the websjef!")

		for registrar in event.eventregistrar_set.all():
			if registrar.paddle_user == registering_user:
				return HttpResponseNotFound("You already registered for this event!")

		if event.get_number_of_free_spots() and event.check_if_registration_not_closed() and event.check_if_registration_started():
			registration = form.save(commit=False)
			registration.paddle_user = registering_user
			registration.event = event
			registration.save()
			event.number_of_attendees += 1
			event.save()
			return super(EventRegisterView, self).form_valid(form)
		else:
			return HttpResponseForbidden()
		


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
		return context


class EventListView(ListView):

	queryset=Event.objects.all()
	template_name = "event_list.html"

	def get_context_data(self, **kwargs):
		events = Event.objects.order_by('start_date').filter(is_published=True, end_date__gte=datetime.now())
		context = super(EventListView, self).get_context_data(**kwargs)
		
		if events:
			context['events'] = events
			try:
				registering_user = PaddleUser.objects.get(user_id=self.request.user.id)
				for event in context['events']:
					event.is_registered = False
					for registrar in event.eventregistrar_set.all():
						if registrar.paddle_user == registering_user:
							event.is_registered = True
							break
			except:
				registering_user = None
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