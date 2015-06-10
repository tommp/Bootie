from django.contrib import admin
from models import BoardMember

class BoardMemberAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields': ['profile_pic', 'position']}),
    ]

admin.site.register(BoardMember, BoardMemberAdmin)