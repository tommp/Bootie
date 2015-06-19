from django.conf.urls import include, url, patterns
from django.contrib import admin

from events.views import EventView, EventListView

urlpatterns = [
    url(r'^$', EventListView.as_view()),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/$', EventView.as_view(), name='event_details'),
]

