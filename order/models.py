from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models  import Token
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.db.models import Sum, F
from multiselectfield import MultiSelectField
# from django.dispatch import receiver
from account.models import CustomUser,Address
from prodect.models import Products
class Order(models.Model):

    STATUS_CHOICES = [
        ('assigned', 'assigned'),
        ('completed', 'completed'),
    ]
    order_coustmerId=models.CharField(max_length=10,default='',blank=True)#رقم العميل صاحب الطلب
    Created_at = models.CharField(max_length=20,default='',blank=True)# type: ignore #تاريخ انشاء الطلب
    delivery_address = models.CharField(max_length=30,default='',blank=True)
    order_status = models.CharField(max_length=20,default='',blank=True)#حالة الطلب
    orderType=models.CharField(max_length=10,null=True,blank=True,)#نوع الطلب استلام للزبون او توصيل
    transaction_reference=models.CharField(max_length=100, default='', blank=True)#رمز العملية نفكر نعمل يخزن باركود 
    payment_status=models.CharField(max_length=10,default='',blank=True)#حالة الدفع
    payment_method=models.CharField(max_length=20, blank=True)#نوع الدفع كاش او الكتروني
    ordersTotalPrice=models.CharField(max_length=10,default='',blank=True)#اجمالي سعر الطلب//
    delivery_charge=models.CharField(max_length=10,default='',blank=True)#رسوم التوصيل
    order_amount=models.CharField(max_length=10,default='',blank=True)#اجمالي عدد الاصناف في الطلبية
    delivery_Employe= models.CharField(max_length=20,default='',blank=True)#ايدي  موظف التوصيل
    commission = models.CharField(max_length=10,default='',blank=True)

    order_number=models.CharField(max_length=20,default='',blank=True)
    note = models.CharField(max_length=50,default='',blank=True)
   
    def calculate_commission(self):
        commission_percentage = 0.2
        commission = float(self.ordersTotalPrice) * commission_percentage
        self.commission = commission
        self.save()

@receiver(post_save, sender=Order)
def calculate_order_commission(sender, instance, created, **kwargs):
    if created:
        instance.calculate_commission()


    class Meta:
        ordering = ['-Created_at']

class OrderDetails(models.Model):
    Prodect_id=models.CharField(max_length=10,blank=False)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    order_number=models.CharField(max_length=10,default='',blank=True)
    price=models.CharField(max_length=10,default='',blank=True)#سعر المنتج من جدول المنتجات
    quntity=models.CharField(max_length=15,default='',blank=True)#الكمية المطلوبة من هاذا المنتج 
    created_at=models.CharField(max_length=20,default='',blank=True)# type: ignore #تاريخ انشاء طلب هاذا المنتج الواحد
    update_at=models.CharField(max_length=20,default='',blank=True)#تاريخ تعديل المنتج
    coustmerid=models.CharField(max_length=10,default='',blank=True)#رقم الايدي العميل صاحب الطلب
    vendor=models.CharField(max_length=10,blank=True)#رقم البائع
    isExist =models.BooleanField(max_length=10,default=False)
   












   