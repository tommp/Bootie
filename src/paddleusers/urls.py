from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views

from paddleusers.views import BoardView
from paddleusers.forms import RegisterView, UserUpdateForm, UserDeleteView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view()),
    url(r'^board/$', BoardView.as_view()),
    url(r'^(?P<pk>\d+)/profile/$', login_required(UserUpdateForm.as_view()), name='user_update_view'),
    url(r'^change_password/$', login_required(views.password_change)),
    url(r'^deactivate_profile/$', login_required(UserDeleteView.as_view()), name='delete_profile'),
    url(r'^profile_deleted_confirm/$', login_required(TemplateView.as_view(template_name='profile_deleted.html')), name='deleted_profile'),
    url(r'^password_changed/$', login_required(TemplateView.as_view(template_name='password_change_success.html')), name='password_change_done'),
]