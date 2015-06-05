from django.shortcuts import render
from django.views.generic import DetailView

from posts.models import Article

class ArticleView(DetailView):

	model = Article
	template_name = "article_details.html"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		if not kwargs.get('pk') or not kwargs.get('slug', '').strip():
			return redirect(self.object, permanent=True)
		
		return super(ArticleView, self).get(request, *args, **kwargs)
