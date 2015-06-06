from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Article

class IndexView(ListView):

	queryset=Article.objects.all()
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['news'] = Article.objects.filter(is_published=True).filter(category='news').order_by('-created')[:3]
		return context