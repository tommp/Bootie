#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

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

class Article(models.Model):
	CATEGORIES = (
		('news', 'News article'),
		('info_general', 'General information'),
		('info_activity', 'Activity information'),
		('info_general_english', 'General information in english'),
		('info_activity_english', 'Activity information in english'),
	)

	created = models.DateTimeField('created', auto_now_add=True)
	updated = models.DateTimeField('updated', auto_now=True)

	is_published = models.BooleanField('is published', help_text="If this is checked, the article is visible in the frontend", default=False)

	slug = models.SlugField('slug', max_length=200, unique=True, blank=True)
	category = models.CharField('category', choices=CATEGORIES, default=CATEGORIES[0][0], blank=True, null=True, max_length=100)


	image = models.ForeignKey('galleries.Image', null=True, blank=True)
	image_description = models.TextField( null=True, blank=True )

	authors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=('authors'), blank=True, related_name='%(app_label)s_%(class)s_authors')

	headline = models.CharField('headline',  max_length=50)
	lead = models.CharField('lead', blank=True, max_length=100)
	body = models.TextField('body', blank=True)

	def __unicode__(self):
		return self.headline

	def save(self, *args, **kwargs):
		self.slug = slugify_unique(self.headline, Article)
		super(Article, self).save(*args, **kwargs)

	def get_list_image(self):
		return self.image
	get_list_image.short_description = "frontpage image"

	def get_share_url(self):
		return 'http://%s%s' % ( Site.objects.get_current(), self.get_absolute_url())
	get_share_url.short_description = "share url"

	def get_authors(self):
		tekst = ""
		if len(self.authors.all()) > 0:
			if len(tekst) > 0:
				tekst += ', '
			tekst += ', '.join([k.get_full_name().strip() for k in self.authors.all()])
			return tekst
		else:
			return tekst
	get_authors.short_description = "get authors"

	def get_absolute_url(self):
		return reverse('article_detail',
					   kwargs={'pk': self.pk, 'slug': self.slug})

