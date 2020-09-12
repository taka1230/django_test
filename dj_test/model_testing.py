import os

import django
from django.core.paginator import Paginator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_test.settings')  # 设置djnago的配置文件
django.setup()
# 注意执行顺序 先执行配置环境 再实例化
# 新增数据的两种方法
# 分页
# 模糊查询 or 多条件用 | 来隔开
# res = models.Nav.objects.filter(Q(name__contains='6')|Q(name__contains='3'))
# print(res)

# models.Nav.objects.create(name='我的日记2')  # 表里插入数据
# models.Nav.objects.create(name='我的日记3')  # 表里插入数据
# models.Nav.objects.create(name='我的日记4')  # 表里插入数据
# models.Nav.objects.create(name='我的日记5')  # 表里插入数据
# models.Nav.objects.create(name='我的日记6')  # 表里插入数据
# models.Nav.objects.create(name='我的日记7')  # 表里插入数据
# nav_obj = models.Nav(name='我的心情1')  # 新增数据的第二种方法
# nav_obj.save()

#  查询数据
#  对象,get方法确认数据是唯一的 不然会报错
# res = models.Nav.objects.get(name='我的心情')
# res2 = models.Nav.objects.get(id=1)
# print(res, type(res))
# print(res.update_time)

# 用于条件查询  不同于get方法 返回的结果可以不唯一 如果有多个并行条件就并行
# res0 = models.Nav.objects.filter(is_delete=1, name='我的心情')  # and条件
# 模糊查询方法：某个字段加上双下划线contains
# 大于gt = great than ; 小于等于 lte = less than equal
# res = models.Nav.objects.filter(name__contains='我的', is_delete__gt=0)  # 大于
# res1 = models.Nav.objects.filter(name__contains='我的', is_delete__gte=0)  # 大于等于
# res2 = models.Nav.objects.filter(name__contains='我的', is_delete__lt=0)  # 小于
# res3 = models.Nav.objects.filter(name__contains='我的', is_delete__lte=0)  # 小于等于
# res4 = models.Nav.objects.filter(name__contains='我的', is_delete=0)  # 等于
# 范围查询
# res5 = models.Nav.objects.filter(id__range=[1, 3])  # range[a,b] a<b
# res6 = models.Nav.objects.filter(id__in=[1, 2, 3, 6])  # 作用等同于sql where in
# # 排除 exclude
# res7 = models.Nav.objects.exclude(id=1)  # 排除id不等于1
# print(res)

# or

# 查询全部数据
# all = models.Nav.objects.all()
# all= models.Nav.objects.all().filter(name__contains='6')
# print(all)

# 修改

# n = models.Nav.objects.get(id=1)
# n = models.Nav.objects.get(pk=1) # primary key 主键
# n.name = '我的相册666'
# n.is_delete = 1
# n.save()

# models.Nav.objects.all().update(is_delete= 0) # 批量修改表数据 all().update()
# models.Nav.objects.filter(name__contains='我的').update(is_delete =1) # 根据条件修改数据 filter().update(


# models.Nav.objects.all().delete() # 删除全部数据

# models.Nav.objects.filter(id__lt=3).delete()  # 按条件删除数据
# from rich import print
# from rich.console import Console
# console = Console()
# console.print("hello", "world", style="bold red")
# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# models.Article.objects.create(title='Django教程1', content='Django教程1', nav_id=1)
# models.Article.objects.create(title='Django教程2', content='Django教程22', nav_id=2)
# models.Article.objects.create(title='Django教程3', content='Django教程333', nav_id=3)
# models.Article.objects.create(title='Django教程4', content='Django教程4444', nav_id=4)

# nav = models.Nav.objects.get(name='我的心情1')
# # print(type(nav))
# models.Article.objects.create(title='Django教程5', content='Django教程55555', nav=nav)
# models.Article.objects.create(title='Django教程6', content='Django教程666666', nav=nav) # 第二种添加方式 使用nav
# models.Article.objects.create(title='Django教程7', content='Django教程7777777', nav=nav)
# models.Article.objects.create(title='Django教程8', content='Django教程88888888', nav=nav)
# 最原始的方法
# nav = models.Nav.objects.get(name='我的日记3')
# result = models.Article.objects.filter(nav=nav)
# print(result)

# 外键反向查询

# nav = models.Nav.objects.get(name='我的心情1')
# res = nav.article_set.all()  # 查询导航下面所有的文章
# # print(res)
#
# art = models.Article.objects.create(title='带傻逼', content='aaa', nav_id=7) # 创建对象
# nav.article_set.add(art)  # 使用表名 + _set.all(a) 新增对象

l = list(range(0, 100))
page_obj = Paginator(l, 20)
print(page_obj.count)  # 总共数据
print(list(page_obj.get_page(2)))  # 获取第一页的数据
print(page_obj.num_pages)  # 一共分了几页 100/5
print(page_obj.page_range)  # 分页范围

page1 = page_obj.get_page(1)
# page1.has_next()  # 判断有没有下一页
# page1.has_other_pages()  # 是否有其他页
# page1.has_previous()  # 是否有上一页
# page1.next_page_number()  # 下一页号码
# page1.previous_page_number()  # 上一页的号码 没有的话报错
page1.end_index()  # 首页页码
page1.start_index()  # 末尾页码
page1.paginator  # 获取分页的对象
