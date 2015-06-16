from django.shortcuts import render
from django.views.generic import ListView
from django.utils.safestring import mark_safe
from eventcalendar.customCalendar import EventCalendar
from posts.models import Article

from datetime import datetime

class IndexView(ListView):

	queryset=Article.objects.all()
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		year = datetime.now().year
		month = datetime.now().month
		events = ""##Events.objects.order_by('my_date').filter(
		#my_date__year=year, my_date__month=month
		#)

		context = super(IndexView, self).get_context_data(**kwargs)
		articles = Article.objects.filter(is_published=True).filter(category='news').order_by('-created')
		if articles:
			context['latest'] = articles[0]
			context['news'] = articles[1:5]
		else:
			context['latest'] = ""
			context['news'] = ""
		context['calendar'] = mark_safe(EventCalendar(events).formatmonth(year, month))
		return context