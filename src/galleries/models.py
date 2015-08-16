# -*- coding: utf-8 -*-

import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.auth.models import User


HT_IS_PUBLISHED = _('Approve this content to be published')
HT_PUBLIC_FROM = _('The date at which the object will be published (still requires "is published" to be ticked)')

class Gallery(models.Model):
    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')
    
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    is_published = models.BooleanField(_('is published'), help_text=HT_IS_PUBLISHED, default=False)
    public_from = models.DateTimeField(_('public from'), help_text=HT_PUBLIC_FROM, blank=False, null=True)

    slug = models.SlugField(_('slug'), max_length=50, unique=True)

    def __unicode__(self):
        return unicode(self.name)


class Image(models.Model):
    class Meta:
        verbose_name=_('image')
        verbose_name_plural=_('images')
        ordering = ('-updated', )

    def __unicode__(self):
        return self.title

    TYPE_CHOICES = (
        ('photo', _('photo')),
        ("illustration", _('illustration')),
    )

    image = models.ImageField(_('image'), upload_to="images/", max_length=255)
    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'), related_name='images', blank=True, null=True)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    credit_user = models.ForeignKey(User, verbose_name=_('credit user'), blank=True, null=True)
    credit_external = models.CharField(_('credit external person'), blank=True, max_length=255)
    image_type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def save(self, *args, **kw):
        self.credit_external = self.credit_external.strip()
        super(Image, self).save(*args, **kw)

    def render(self, caption, alignment="right"):
        template = 'galleries/models/image_render.html'
        context = {
            'image': self,
            'caption': caption,
            'alignment': alignment,
            'bottom_bar': caption or self.get_credit()
        }

        return render_to_string(template, context)

    def get_credit(self):
        if self.credit_user:
            html = self.credit_user.get_full_name()
        elif self.credit_external:
            html = self.credit_external
        else:
            html = ''
        return mark_safe(html)
    get_credit.shord_description = 'credit'
