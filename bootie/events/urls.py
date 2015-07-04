from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.decorators.http import require_POST

from events.views import EventView, EventListView, EventRegisterView, AttendeesView

urlpatterns = [
    url(r'^$', EventListView.as_view()),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/$', EventView.as_view(), name='event_details'),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/register/$', EventRegisterView.as_view(), name='event_register_view'),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/attendees/$', AttendeesView.as_view(), name='attendees_view'),
]

