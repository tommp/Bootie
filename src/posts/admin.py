from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields': ['is_published', 'image', 'category', 'headline', 'lead', 'body', 'authors']}),
    ]

admin.site.register(Article, ArticleAdmin)
