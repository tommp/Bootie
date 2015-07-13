from django.shortcuts import render
from django.views.generic import DetailView, ListView
from datetime import datetime

from posts.models import Article

class ArticleView(DetailView):

	model = Article
	template_name = "article_details.html"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		if not kwargs.get('pk') or not kwargs.get('slug', '').strip():
			return redirect(self.object, permanent=True)
		
		return super(ArticleView, self).get(request, *args, **kwargs)

class NewsView(ListView):
	queryset=Article.objects.all()
	template_name = "news.html"

	def get_context_data(self, **kwargs):
		year = datetime.now().year
		month = datetime.now().month

		context = super(NewsView, self).get_context_data(**kwargs)
		articles = Article.objects.filter(is_published=True).filter(category='news').order_by('-created')
		if articles:
			context['leftCol'] = articles[0::2]
			context['rightCol'] = articles[1::2]
		else:
			context['news'] = ""
		return context