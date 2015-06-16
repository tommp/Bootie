from django.contrib import admin
from models import PaddleUser, Position

class PaddleUserAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields': ['profile_pic', 'user', 'paid_until', 'banned']}),
    ]

class PositionAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields': ['name', 'user']}),
    ]

admin.site.register(PaddleUser, PaddleUserAdmin)
admin.site.register(Position, PositionAdmin)