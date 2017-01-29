from django.views.generic import ListView
from posts.models import Article
from events.models import Event
from ads.models import Ad

from datetime import datetime


class IndexView(ListView):
    queryset = Article.objects.all()
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        year = datetime.now().year
        month = datetime.now().month

        context = super(IndexView, self).get_context_data(**kwargs)

        articles = Article.objects.filter(is_published=True).filter(category='news').order_by('-created')
        ads = Ad.objects.filter(is_published=True).order_by('-priority')

        if articles:
            context['articles'] = articles[0:10]
        else:
            context['articles'] = []

        if ads:
            context['ads'] = ads[0:5]
        else:
            context['ads'] = []

        return context
