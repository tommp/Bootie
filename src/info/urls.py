from django.conf.urls import include, url, patterns
from django.contrib import admin

from info.views import InfoView, EnglishInfoView

urlpatterns = [
    url(r'^$', InfoView.as_view()),
    url(r'^english/', EnglishInfoView.as_view()),
]