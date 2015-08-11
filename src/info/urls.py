from django.conf.urls import include, url, patterns
from django.contrib import admin

from info.views import InfoView

urlpatterns = [
    url(r'^$', InfoView.as_view()),
]