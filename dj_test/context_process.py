from user import models
from user import const
def nav_title_process(request):
    """上下文管理器，这个函数里面返回的每个变量 在每个页面都可以用"""
    # navs = ['我的相册', '我的日记', 'python', 'linux','接口测试']
    navs = models.Nav.objects.filter(is_delete=1)
    title = "taka's blog"
    content = {'daohang': navs,
               'title': title,
               'page_limit': const.page_limit
    }
    return content
