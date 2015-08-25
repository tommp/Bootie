from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView

from index.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^instagram/$', TemplateView.as_view(template_name="instagram.html")),
]
