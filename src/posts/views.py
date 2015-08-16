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
	queryset=Article.objects.filter(is_published=True).filter(category='news').order_by('-created')
	template_name = "news.html"
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super(NewsView, self).get_context_data(**kwargs)

		articles = context['page_obj']

		if articles:
			context['leftCol'] = articles[1::2]
			context['rightCol'] = articles[0::2]
		else:
			context['news'] = ""
		return context