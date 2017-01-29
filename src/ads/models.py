from django.db import models
from galleries.models import Image
from django.conf import settings


class Ad(models.Model):
    name = models.CharField('ad name', blank=False, max_length=100)

    priority = models.FloatField('priority', default=0)

    created = models.DateTimeField('created', auto_now_add=True)
    updated = models.DateTimeField('updated', auto_now=True)

    is_published = models.BooleanField('is published', help_text="If this is checked, the ad is visible in the frontend", default=False)

    url = models.CharField('link name', blank=False, max_length=200)

    image = models.ForeignKey('galleries.Image', null=True, blank=True)

    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=('authors'), blank=True, related_name='%(app_label)s_%(class)s_authors')

    def __unicode__(self):
        return self.name

    def get_list_image(self):
        return self.image.image
    get_list_image.short_description = "frontpage image"

    def get_advertisers_link(self):
        return self.url
