from django.db import models
from galleries.models import Image
from django.utils.translation import ugettext_lazy as _


class FrontpageContext(models.Model):
    class Meta:
        verbose_name = _('frontpage context')
        verbose_name_plural = _('frontpage contexts')

    name = models.CharField(_('name'), max_length=255)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    top_logo = models.ForeignKey('galleries.Image', related_name="top_logo", null=True, blank=True)
    facebookImage = models.ForeignKey('galleries.Image', related_name="face_image", null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)
