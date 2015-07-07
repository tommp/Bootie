from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views

from paddleusers.views import RegisterView, BoardView, UserUpdateForm

urlpatterns = [
    url(r'^register/$', RegisterView.as_view()),
    url(r'^board/$', BoardView.as_view()),
    url(r'^(?P<pk>\d+)/profile/$', login_required(UserUpdateForm.as_view()), name='user_update_view'),
    url(r'^change-password/$', views.password_change),
    url(r'^password-changed/$', TemplateView.as_view(template_name='password_change_success.html'), name='password_change_done'),
]