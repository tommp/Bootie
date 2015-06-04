from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Article(models.Model):
    CATEGORIES = (
        ('info', 'Information archive'),
        ('news', 'News article'),
    )

    created = models.DateTimeField('created', auto_now_add=True)
    updated = models.DateTimeField('updated', auto_now=True)

    is_published = models.BooleanField('is published', help_text="If this is checked, the article is visible in the frontend", default=False)

    slug = models.SlugField('slug', max_length=200, unique=True, blank=True)
    category = models.CharField('category', choices=CATEGORIES, blank=True, null=True, max_length=100)

    image = models.ImageField('image', null=True, blank=True)
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
