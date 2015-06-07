#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings

class Article(models.Model):
    CATEGORIES = (
        ('news', 'News article'),
        ('info_general', 'General information'),
        ('info_activity', 'Activity information'),
    )

    created = models.DateTimeField('created', auto_now_add=True)
    updated = models.DateTimeField('updated', auto_now=True)

    is_published = models.BooleanField('is published', help_text="If this is checked, the article is visible in the frontend", default=False)

    slug = models.SlugField('slug', max_length=200, unique=True, blank=True)
    category = models.CharField('category', choices=CATEGORIES, default=CATEGORIES[0][0], blank=True, null=True, max_length=100)

    image = models.ImageField('image', upload_to="images/", null=True, blank=True)
    image_description = models.TextField( null=True, blank=True )

    headline = models.CharField('headline',  max_length=100)
    lead = models.TextField('lead', blank=True)
    body = models.TextField('body', blank=True)

    def __unicode__(self):
        return self.headline


    def get_list_image(self):
        return self.image
    get_list_image.short_description = "frontpage image"

    def get_share_url(self):
        return 'http://%s%s' % ( Site.objects.get_current(), self.get_absolute_url())
    get_share_url.short_description = "share url"

    def get_absolute_url(self):
        return reverse('article_detail',
                       kwargs={'pk': self.pk, 'slug': self.slug})




#class PaddleUser(models.Model):
#     TITLES = (
#        ('Leder', 'Leder'),
#        ('Leder', 'Nestleder'),
#        ('Økonomisjef', 'Økonomisjef'),
#        ('Elvesjef','Elvesjef'),
#        ('Havsjef','Havsjef'),
#        ('Websjef','Websjef'),
#        ('Utstyrssjef hav','Utstyrssjef hav'),
#        ('Utstyressjef elv','Utstyressjef elv'),
#        ('Polosjef','Polosjef'),
#        ('Websjef','Websjef'),
#        ('Sosialansvarlig','Sosialansvarlig'),
#        ('Styremedlem','Styremedlem'),
#    )
#    user = models.OneToOneField(settings.AUTH_USER_MODEL)
#    profile_pic = models.ImageField('profile picture', upload_to="images/", null=True, blank=True)
#    user = models.ForeignKey(models.CharField, choices=TITLES, blank=True, null=True, max_length=100)