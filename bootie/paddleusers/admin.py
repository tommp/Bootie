from django.contrib import admin
from models import PaddleUser

class PaddleUserAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields': ['profile_pic', 'user', 'paid_until', 'banned']}),
    ]

admin.site.register(PaddleUser, PaddleUserAdmin)