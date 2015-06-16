#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django.db import models
from django.conf import settings
from datetime import datetime

class PaddleUser(models.Model):


	created = models.DateTimeField('Created', auto_now_add=True)
	paid_until = models.DateTimeField('Equipment rental valid until')

	profile_pic = models.ImageField('Profile picture', upload_to="images/", null=True, blank=True)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

	banned = models.BooleanField('Banned', help_text="If this is checked, the user is banned and can no longer sign up for events and will not recieve the code for skansen.", default=False)

	def __unicode__(self):
		return self.user.username

	def get_list_image(self):
		return self.profile_pic
	get_list_image.short_description = "Profile picture"

	@classmethod
	def create(cls, profile_pic, user, paid_until):
		user = cls(profile_pic=profile_pic, user=user, paid_until=paid_until)
		return user


class Position(models.Model):
	name =  models.CharField('Board position', max_length=100)
	user = models.ForeignKey('PaddleUser', blank=True)

	def __unicode__(self):
		return self.name

