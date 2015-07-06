import datetime
import copy

from django import forms
from django.views.generic.edit import FormView
from events.models import Event, EventRegistrar
from dateutil.relativedelta import relativedelta

class EventForm(forms.ModelForm):

	TYPES = (
		('weekly', 'Weekly'),
		('daily', 'Daily'),
		('monthly', 'Monthly'),
		('yearly', 'Yearly'),
	)

	class Meta:
		model = Event
		fields = ('is_published', 'show_attendees', 'name', 'start_date', 'end_date', 'registration_open_date', 
		'registration_cutoff_date', 'cancellation_cutoff_date', 'repeats', 'repeat_type',
		'category', 'image', 'image_description', 'event_article', 'max_attendees', 'cost')

	repeats = forms.IntegerField(min_value=0, initial=0)
	repeat_type = forms.ChoiceField(choices=TYPES)

	def save(self, commit=True):
		saved_event = super(EventForm, self).save(commit=commit)
		repeat_type_clean = self.cleaned_data.get('repeat_type', None)
		repeats_clean = self.cleaned_data.get('repeats', None)
		for i in range(repeats_clean):
			if repeat_type_clean == 'weekly':
				saved_event.start_date += relativedelta(weeks=1)
				saved_event.end_date += relativedelta(weeks=1)
				saved_event.registration_open_date += relativedelta(weeks=1)
				saved_event.registration_cutoff_date += relativedelta(weeks=1)
				saved_event.cancellation_cutoff_date += relativedelta(weeks=1)
			elif repeat_type_clean == 'daily':
				saved_event.start_date += relativedelta(days=1)
				saved_event.end_date += relativedelta(days=1)
				saved_event.registration_open_date += relativedelta(days=1)
				saved_event.registration_cutoff_date += relativedelta(days=1)
				cancellation_cutoff_date += relativedelta(days=1)
			elif repeat_type_clean == 'monthly':
				saved_event.start_date += relativedelta(months=1)
				saved_event.end_date += relativedelta(months=1)
				saved_event.registration_open_date += relativedelta(months=1)
				saved_event.registration_cutoff_date += relativedelta(months=1)
				saved_event.cancellation_cutoff_date += relativedelta(months=1)
			else:
				saved_event.start_date += relativedelta(years=1)
				saved_event.end_date += relativedelta(years=1)
				saved_event.registration_open_date += relativedelta(years=1)
				saved_event.registration_cutoff_date += relativedelta(years=1)
				saved_event.cancellation_cutoff_date += relativedelta(years=1)
			saved_event.pk = None
			saved_event.save()
		return super(EventForm, self).save(commit=commit)
