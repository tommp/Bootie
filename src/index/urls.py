from django.conf.urls import include, url, patterns
from django.contrib import admin

from index.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
]
