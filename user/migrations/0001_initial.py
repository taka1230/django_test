# Generated by Django 2.2 on 2020-07-20 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='导航名称')),
                ('is_delete', models.SmallIntegerField(default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '导航表',
                'verbose_name_plural': '导航表',
                'db_table': 'nav',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, unique=True, verbose_name='导航名称')),
                ('content', models.TextField(null=True, verbose_name='文章内容')),
                ('img', models.ImageField(null=True, upload_to='article_img', verbose_name='图片文章')),
                ('is_delete', models.SmallIntegerField(default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('nav', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Nav', verbose_name='导航id')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
