from django.conf.urls import include, url, patterns
from django.contrib import admin

from posts.views import ArticleView, NewsView

urlpatterns = [
    url(r'^$', ArticleView.as_view()),
    url(r'^(?P<pk>\d+)/(?P<slug>[^/]+?)/$', ArticleView.as_view(), name='article_detail'),
    url(r'^news/$', NewsView.as_view(), name='news_list'),
]

