from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


from events.views import EventView, EventListView, EventRegisterView, AttendeesView, EventUnRegisterView

urlpatterns = [
    url(r'^$', EventListView.as_view()),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/$', EventView.as_view(), name='event_details'),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/register/$', login_required(EventRegisterView.as_view()), name='event_register_view'),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/unregister/$', login_required(EventUnRegisterView.as_view()), name='event_unregister_view'),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/attendees/$', login_required(AttendeesView.as_view()), name='attendees_view'),
]

