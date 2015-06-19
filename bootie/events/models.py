from django.db import models
from posts.models import Article
from paddleusers.models import PaddleUser
from django import forms
from django.views.generic.edit import FormView
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

def slugify_unique(value, model, slugfield="slug"):
	"""
	copied from
	http://stackoverflow.com/questions/1490559/django-slugified-urls-how-to-handle-collisions
	"""
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
	image = models.ImageField('image', upload_to="images/", null=True)

	def __unicode__(self):
		return self.name

	def get_list_image(self):
		return self.image
	get_list_image.short_description = "category image"

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

	registered_users = models.ManyToManyField('paddleusers.PaddleUser', blank=True)

	image = models.ImageField('image', upload_to="images/", null=True, blank=True)
	image_description = models.TextField( null=True, blank=True )

	event_article = models.ForeignKey('posts.Article')

	max_attendees = models.IntegerField(default = 0)
	number_of_attendees = models.IntegerField(default = 0)

	cost = models.IntegerField(default = 0)

	show_attendees = models.BooleanField('Show attendees', default=True)

	def __unicode__(self):
		return self.name + ' (' + str(self.start_date.day) + '.' + str(self.start_date.month) + '.' + str(self.start_date.year) + ')'

	def get_list_image(self):
		return self.image
	get_list_image.short_description = "frontpage image"

	def get_share_url(self):
		return 'http://%s%s' % ( Site.objects.get_current(), self.get_absolute_url())
	get_share_url.short_description = "share url"

	def get_number_of_free_spots(self):
		return self.max_attendees - self.number_of_attendees

	def get_absolute_url(self):
		return reverse('event_details',
					   kwargs={'pk': self.pk, 'slug': self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify_unique(self.name, Event)
		super(Event, self).save(*args, **kwargs)