from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("headline",),}
	fieldsets = [
	( None, {'fields': ['is_published', 'image', 'headline', 'lead', 'body']}),
    ('Additional options', {'fields': ['slug'], 'classes': ['collapse']}),
    ]

admin.site.register(Article, ArticleAdmin)
