from django.db import models
from posts.models import Article
from paddleusers.models import PaddleUser
from django import forms
from django.views.generic.edit import FormView
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.utils import timezone

from galleries.models import Image

def slugify_unique(value, model, slugfield="slug"):
	suffix = 0
	potential = base = slugify(value)
	while True:
		if suffix:
			potential = "-".join([base, str(suffix)])
		if not model.objects.filter(**{slugfield: potential}).count():
			return potential
		suffix += 1

class Category(models.Model):
	class Meta:
		verbose_name='category'
		verbose_name_plural='categories'
		ordering=['-name']
		
	name = models.CharField('category', blank=False, max_length=100)
	image = models.ForeignKey('galleries.Image', null=True)

	def __unicode__(self):
		return self.name

	def get_list_image(self):
		return self.image
	get_list_image.short_description = "category image"

	

class EventRegistrar(models.Model):
	car_seats = models.IntegerField(default=0)
	paddle_user = models.ForeignKey('paddleusers.PaddleUser')
	event = models.ForeignKey('Event')

	def __unicode__(self):
		return self.paddle_user.user.first_name + self.paddle_user.user.last_name

	def __unicode__(self):
		return self.paddle_user.user.username

	def get_full_name(self):
		return self.paddle_user.user.first_name + self.paddle_user.user.last_name

	def get_email(self):
		return self.paddle_user.user.email


class Event(models.Model):

	name = models.CharField('event name', blank=False, max_length=100)

	created = models.DateTimeField('created', auto_now_add=True)
	updated = models.DateTimeField('updated', auto_now=True)

	start_date = models.DateTimeField('start time')
	end_date = models.DateTimeField('end time')

	registration_open_date = models.DateTimeField('registration open time')
	registration_cutoff_date = models.DateTimeField('registration cutoff time')

	cancellation_cutoff_date = models.DateTimeField('cancellation cutoff time')

	is_published = models.BooleanField('is published', help_text="If this is checked, the event is visible in the frontend", default=False)

	slug = models.SlugField('slug', max_length=200, unique=True)
	category = models.ManyToManyField('Category')

	image = models.ForeignKey('galleries.Image', null=True, blank=True)
	image_description = models.TextField( null=True, blank=True )

	event_article = models.ForeignKey('posts.Article')

	max_attendees = models.IntegerField(default = 0, help_text="Leave at 0 to disable registration")
	number_of_attendees = models.IntegerField(default = 0)

	cost = models.IntegerField(default = 0)

	show_attendees = models.BooleanField('Show attendees', default=True)

	def __unicode__(self):
		return self.name + ' (' + str(self.start_date.day) + '.' + str(self.start_date.month) + '.' + str(self.start_date.year) + ')'

	def get_list_image(self):
		return self.image.image
	get_list_image.short_description = "frontpage image"

	def get_share_url(self):
		return 'http://%s%s' % ( Site.objects.get_current(), self.get_absolute_url())
	get_share_url.short_description = "share url"

	def check_if_cancellation_availible(self):
		if self.cancellation_cutoff_date > timezone.now():
			return True
		return False

	def check_if_registration_not_closed(self):
		if self.registration_cutoff_date > timezone.now():
			return True
		return False

	def check_if_registration_started(self):
		if self.registration_open_date < timezone.now():
			return True
		return False

	def get_number_of_free_spots(self):
		return self.max_attendees - self.number_of_attendees

	def get_absolute_url(self):
		return reverse('event_details',
					   kwargs={'pk': self.pk, 'slug': self.slug})

	def get_registration_url(self):
		return reverse('event_details',
					   kwargs={'pk': self.pk, 'slug': self.slug}) + "register"

	def get_unregistration_url(self):
		return reverse('event_details',
					   kwargs={'pk': self.pk, 'slug': self.slug}) + "unregister"

	def get_attendees_url(self):
		return reverse('event_details',
					   kwargs={'pk': self.pk, 'slug': self.slug}) + "attendees"

	def save(self, *args, **kwargs):
		self.slug = slugify_unique(self.name, Event)
		super(Event, self).save(*args, **kwargs)