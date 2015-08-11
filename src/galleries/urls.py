from django.conf.urls import patterns, url

urlpatterns = patterns('galleries.views',
            url(r'^$', 'gallery', name='ud-galleries'),
            url(r'^(?P<slug>[-\w]+)/$', 'gallery'),
)
