from django.shortcuts import render, HttpResponse
from user import models
from django.core.paginator import Paginator
from .const import page_limit
# Create your views here.
def index(request):
    limit = request.GET.get('limit', page_limit)  # get kv值 默认值为20 限制20条
    page = request.GET.get('page', 1)
    page_obj =  Paginator(models.Article.objects.all().order_by('id'), limit)
    page_data = page_obj.get_page(page)
    dic = {'articles': page_data}
    # print(page_obj.num_pages)
    return render(request, 'index.html', dic)


def info(request, id):
    article = models.Article.objects.get(id=id)
    dic = {"article":article}
    return render(request, 'info.html', dic)

def nav_article(request, id):
    nav = models.Nav.objects.get(id=id)  # 查到导航
    articles = nav.article_set.all().filter(is_delete=1)  # 查到导航下面所有的文章
    dic = {'articles': articles}
    return render(request, 'index.html', dic)

def test(request):
    pass