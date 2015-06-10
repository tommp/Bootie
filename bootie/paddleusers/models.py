#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django.db import models
from django.conf import settings

class BoardMember(models.Model):
	TITLES = (
		('Leder', 'Leder'),
		('Nestleder', 'Nestleder'),
		('Økonomisjef', 'Økonomisjef'),
		('Elvesjef','Elvesjef'),
		('Havsjef','Havsjef'),
		('Websjef','Websjef'),
		('Utstyrssjef hav','Utstyrssjef hav'),
		('Utstyressjef elv','Utstyressjef elv'),
		('Polosjef','Polosjef'),
		('Websjef','Websjef'),
		('Sosialansvarlig','Sosialansvarlig'),
		('Styremedlem','Styremedlem'),
	)

	pic = models.ImageField('Profile picture', upload_to="images/", null=True, blank=True)
	position = models.CharField('Board position', choices=TITLES, blank=True, null=True, max_length=100)

	def __unicode__(self):
		return self.position

	def get_list_image(self):
		return self.profile_pic
	get_list_image.short_description = "Profile picture"