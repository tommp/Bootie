from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Article

class InfoView(ListView):

	queryset=Article.objects.all()
	template_name = "info.html"

	def get_context_data(self, **kwargs):
		context = super(InfoView, self).get_context_data(**kwargs)
		context['activities'] = Article.objects.filter(is_published=True).filter(category='info_activity').order_by('-created')
		context['general_articles'] = Article.objects.filter(is_published=True).filter(category='info_general').order_by('-created')
		return context