from django.contrib import admin
from ads.models import Ad


class AdAdmin(admin.ModelAdmin):

    fieldsets = [
    (None, {'fields': [
        'is_published',
        'name',
        'priority',
        'url',
        'image',
        'authors']}),
    ]


admin.site.register(Ad, AdAdmin)
