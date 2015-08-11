from django.db import models
from django.contrib import admin

from galleries.models import Gallery, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    fieldsets = [
        (None,                  {'fields': ['name', 'description', 'slug']}),
        ('Publish information', {'fields': ['is_published', 'public_from'], 'classes': ['collapse']}),
        ('Date information',    {'fields': ['created', 'updated'], 'classes': ['collapse']}),
    ]
    readonly_fields = ('created', 'updated')
    inlines = [
        ImageInline
    ]

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_credit', 'created', 'updated')
    fieldsets = [
        (None,                  {'fields': ['image','gallery']}),
        ('Date information',    {'fields': ['created', 'updated'], 'classes': ['collapse']}),
        ('Image information',   {'fields': ['title', 'description', 'credit_user',  'credit_external', 'image_type']}),
    ]
    readonly_fields = ('created', 'updated')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
