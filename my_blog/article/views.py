from django.shortcuts import render
from django.http import HttpResponse, Http404
from article.models import Article
from datetime import datetime
from django.core import serializers

# Create your views here.


def home(request):
    post_list = Article.objects.all()
    with open('a.txt','w') as f:
        f.writelines(serializers.serialize('json', post_list))
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