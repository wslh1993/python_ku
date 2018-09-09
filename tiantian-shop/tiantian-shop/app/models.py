from django.db import models
from django.core import validators
import datetime


class User(models.Model):
    """用户信息"""
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    username = models.CharField(
        verbose_name='用户名', unique=True, max_length=30,
        validators=[validators.MinLengthValidator(limit_value=6, message='用户名不能少于6位')]
    )
    password = models.CharField(
        verbose_name='密码', max_length=30,
        validators=[
            validators.MinLengthValidator(limit_value=8, message='密码不能少于8位')
        ]
    )
    email = models.EmailField(
        verbose_name='邮箱', unique=True
    )

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=['username'])

class OrderInfo(models.Model):
    """订单信息"""
    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    status = models.SmallIntegerField('订单状态', choices=[(0, '未确认'), (1, '确认'), (2, '已取消'), (3, '无效'), (4, '退货')])
    pay_status = models.SmallIntegerField('支付状态', choices=[(0, '未付款'), (1, '付款中'), (2, '已付款')])
    shipping_status = models.SmallIntegerField('配送状态', choices=[(0, '未发货'), (1, '已发货'), (2, '已收货'), (3, '退货 ')])
    add_time = models.DateTimeField('创建时间', auto_now_add=True)

class OrderGoods(models.Model):
    """订单商品（订单和商品是多对多关系，该表是中间表）"""
    order_info = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name='订单ID')
    goods = models.ForeignKey('Goods',on_delete=models.CASCADE)
    number = models.SmallIntegerField('数量')
    add_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_update = models.DateTimeField('最后更新', auto_now=True)


class Userinfo(models.Model):
    '''用户信息表，输入地址相关'''
    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name
    address = models.CharField('地址',null=False,max_length=100,default='23')
    phone = models.CharField('电话',null=False,max_length=11,default='123')
    recipient = models.CharField('收件人',null=False,max_length=10,default='1223')
    postcode = models.CharField('邮编',null=False,max_length=6,default='123')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    def __str__(self):
        return self.name
class Category(models.Model):
    """分类信息"""
    name = models.CharField('名称', max_length=10, unique=True)
    icon = models.CharField('图片样式', max_length=20)


def upload_thumb(instance, filename):
    return '{0}_{1}.png'.format(
            instance.id, datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        )


class Goods(models.Model):
    """商品信息"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=30)
    price = models.DecimalField('价格', max_digits=5, decimal_places=2)
    thumb = models.ImageField('主图', upload_to=upload_thumb, null=True, blank=True)


class Cart(models.Model):
    """购物车"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods, through='CartGoods', through_fields=('cart', 'goods'))


class CartGoods(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    number = models.SmallIntegerField(default=0)
