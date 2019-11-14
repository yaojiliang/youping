from django.db import models

# Create your models here.
from qiantai.models import UserInfo, Goods


class Order(models.Model):
    order_id=models.AutoField('订单id',primary_key=True)
    order_time=models.DateTimeField('订单时间',auto_now_add=True)
    total_price=models.DecimalField('订单总额',max_digits=8,decimal_places=2)
    user=models.ForeignKey(UserInfo)
    good = models.ForeignKey(Goods)
    class Meta:
        db_table='order'

class Order_info(models.Model):
    rec_id=models.AutoField('订单详细信息',primary_key=True)
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    good=models.ForeignKey(Goods,on_delete=models.CASCADE)
    class Meta:
        db_table='order_info'
