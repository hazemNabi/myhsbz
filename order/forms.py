from django import forms
from order.models import *
from django.contrib.auth import get_user_model

from django.forms import ModelForm


class changeOrderStatus(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status']
        widgets={
           'order_status':forms.Select(attrs={'class':'form-control pull-right'},),
        }