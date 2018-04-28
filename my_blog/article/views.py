from django.shortcuts import render
from django.http import HttpResponse, Http404
from article.models import Article
from datetime import datetime
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.syndication.views import Feed
from django.core.paginator import Page,EmptyPage, InvalidPage,Paginator, PageNotAnInteger

# Create your views here.


def home(request):
    post_list = Article.objects.all()
    paginator = Paginator(post_list, 2)
    p = request.GET.get('p')
    try:
        post_list = paginator.page(p)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


# 尝试访问数据库
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExsit:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def archives(request):
    article_lists =  Article.objects.all()
    return render(request,'archive.html',{'article_lists':article_lists, 'error': False})


def about_me(request):
    return render(request, 'about_me.html')


def search_tag(request, tag):
    post_lists = Article.objects.filter(category=tag)
    return render(request, 'tag.html', {'post_lists': post_lists})


def blog_search(request):
    if 's' in request.GET:
        search_key = request.GET.get('s')
        if not search_key:
            return render(request, 'home.html')
        else:
            article_lists = Article.objects.filter(title__contains=search_key)
            if len(article_lists) == 0:
                return render(request, 'archive.html', {'article_lists': article_lists, 'error': True})
            else:
                return render(request, 'archive.html', {'article_lists': article_lists, 'error': False})
    redirect('/home/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content

