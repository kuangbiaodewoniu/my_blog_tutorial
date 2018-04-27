from django.shortcuts import render
from django.http import HttpResponse
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
def detail(request):
    article_1 = Article.objects.all()[0]
    return HttpResponse('title= %s, category= %s, content= %s' %(article_1.title, article_1.category, article_1.content))


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})