from django.shortcuts import render
from django.views.generic import ListView
from django.utils.safestring import mark_safe
from events.eventCalendar import EventCalendar
from posts.models import Article
from events.models import Event

from datetime import datetime

class IndexView(ListView):

	queryset=Article.objects.all()
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		year = datetime.now().year
		month = datetime.now().month
		events = Event.objects.order_by('start_date').filter(start_date__year=year, start_date__month=month)

		context = super(IndexView, self).get_context_data(**kwargs)
		articles = Article.objects.filter(is_published=True).filter(category='news').order_by('-created')
		if articles:
			context['latest'] = articles[0]
			context['news_left'] = articles[1]
			context['news_right'] = articles[2]
		else:
			context['latest'] = ""
			context['news_left'] = ""
			context['news_right'] = ""
		context['calendar'] = mark_safe(EventCalendar(events).formatmonth(year, month))
		return context