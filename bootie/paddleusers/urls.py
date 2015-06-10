from django.conf.urls import include, url, patterns
from django.contrib import admin

from paddleusers.views import RegisterView

urlpatterns = [
    url(r'^$', RegisterView.as_view()),
]