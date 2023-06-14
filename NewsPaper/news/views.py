from django.views.generic import ListView, DetailView
from .models import Article


class ArticlesList(ListView):
    model = Article
    ordering = '-date'
    template_name = 'articles.html'
    context_object_name = 'article'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
