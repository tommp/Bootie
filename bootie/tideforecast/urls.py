from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="tide.html")),
]
