from django.contrib import admin
from events.models import Event, Category
from events.forms import EventForm


class EventAdmin(admin.ModelAdmin):

	form = EventForm
	fieldsets = [
	( None, {'fields': ['is_published', 'show_attendees', 'name', 'start_date', 'end_date', 'registration_open_date', 
		'registration_cutoff_date', 'cancellation_cutoff_date', 'repeats', 'repeat_type',
		'category',  'image', 'image_description', 'event_article', 'max_attendees', 'cost']}),
	]

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields': ['name', 'image']}),
	]


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)