# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-13 01:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False, verbose_name='品牌id')),
                ('brand_desc', models.TextField(verbose_name='品牌简介')),
                ('brand_name', models.CharField(max_length=32, verbose_name='品牌名称')),
                ('brand_pic', models.ImageField(default='', upload_to='brand_img', verbose_name='品牌图片')),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品id')),
                ('goods_name', models.CharField(max_length=50, verbose_name='商品名称')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格')),
                ('goods_img', models.ImageField(default='', upload_to='good_img', verbose_name='商品图片')),
                ('goods_desc', models.TextField(verbose_name='商品描述')),
                ('goods_num', models.IntegerField(verbose_name='商品数量')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qiantai.Brand')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('username', models.CharField(max_length=11, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('user_telphone', models.CharField(max_length=11, verbose_name='电话')),
                ('user_point', models.IntegerField(default=100, verbose_name='用户积分')),
                ('userEmail', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('user_create_time', models.DateTimeField(auto_now_add=True, verbose_name='用户创建时间')),
                ('user_last_Visiitetime', models.DateTimeField(auto_now_add=True, verbose_name='最后访问时间')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]