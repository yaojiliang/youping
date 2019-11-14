from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_id=models.AutoField('用户id',primary_key=True)
    username=models.CharField('用户名',max_length=11,unique=True)
    password=models.CharField('密码',max_length=32)
    # user_realname=models.CharField('真实姓名',max_length=16,null=True)
    user_telphone=models.CharField('电话',max_length=11)
    # 手机可以是唯一但是为了测试　unique=True
    user_point=models.IntegerField('用户积分',default=100)
    userEmail=models.EmailField('邮箱',unique=True)
    user_create_time=models.DateTimeField('用户创建时间',auto_now_add=True)
    user_last_Visiitetime=models.DateTimeField('最后访问时间',auto_now_add=True)
    class Meta:
        db_table='user_info'


class Brand(models.Model):
    brand_id=models.AutoField('品牌id',primary_key=True)
    brand_desc=models.TextField('品牌简介')
    brand_name=models.CharField('品牌名称',max_length=32)
    brand_pic=models.ImageField('品牌图片',upload_to='brand_img',default='')

    class Meta:
        db_table='brand'


class Goods(models.Model):
    goods_id = models.AutoField('商品id', primary_key=True)
    goods_name = models.CharField('商品名称', max_length=50, )
    market_price = models.DecimalField('价格', max_digits=6, decimal_places=2)
    goods_img = models.ImageField('商品图片', upload_to='good_img', default='')
    goods_desc = models.TextField('商品描述')
    goods_num = models.IntegerField('商品数量')
    brand = models.ForeignKey(Brand)
    class Meta:
        db_table='goods'


