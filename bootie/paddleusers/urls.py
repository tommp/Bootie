from django.conf.urls import include, url, patterns
from django.contrib import admin

from paddleusers.views import RegisterView, BoardView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view()),
    url(r'^board/$', BoardView.as_view()),
]