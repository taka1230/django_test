from django.db import models


#  python3 manage.py makemigrations 产生迁移数据库的代码
#  python3 manage.py migrate 建表

# Create your models here.
class Nav(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='导航名称')  # 定义字符串 长度为10 不唯一 并且不能为空 如果为空 null=True
    is_delete = models.SmallIntegerField(default=1, verbose_name='是否被删除')  # 不做物理删除 只做逻辑删除
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 插入数据的时间 设置为当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 修改数据的时间为当前时间

    def __str__(self):
        """此处是为了查询的时候 返回表里的name字段
        当然也可以返回其他的字段"""
        return self.name

    class Meta:
        verbose_name = '导航表'
        verbose_name_plural = verbose_name
        db_table = 'nav'
        # ordering = ['update_time']  # 查询数据的时候，用来排序的


class Article(models.Model):
    title = models.CharField(max_length=10, unique=True, verbose_name='导航名称')  # 定义字符串 长度为10 不唯一 并且不能为空 如果为空 null=True
    content = models.TextField(null=True, verbose_name='文章内容')
    img = models.ImageField(upload_to='article_img', null=True, verbose_name='图片文章', default='article_img/1.jpg')
    nav = models.ForeignKey(Nav, verbose_name='导航id', on_delete=models.DO_NOTHING,
                            db_constraint=False)  # 不建立外键关系 否则不能删除外键 还会影响性能,do_nothing代表着如果删除导航 不删除相对应的文章
    is_delete = models.SmallIntegerField(default=1, verbose_name='是否被删除')  # 不做物理 删除 只做逻辑删除
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 插入数据的时间 设置为当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 修改数据的时间为当前时间

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'

# 修改表结构 删除migrations文件夹下 除去__init__以外的文件
# python3 manage.py makemigration {appname}
# python3 manage.py sqlmigrate {appname} 0001 查看生成的迁移数据库的sql
# python3 manage.oy migrate 或者 把sql提出来 在数据库暴力建表
