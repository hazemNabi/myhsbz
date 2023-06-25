from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect ,get_object_or_404

from account.models import CustomUser
from prodect.models import Products
from order.forms import changeOrderStatus
from order.models import Order,OrderDetails
from django.db.models import Count

# Create your views here.

from .models import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.db.models import Sum

def details(request, id):
    order = get_object_or_404(Order, id=id)
    order_details = OrderDetails.objects.filter(order_id=order.pk)
    total = 0
    # for sub in order_details:
    #     total += sub.price * 2
    commissions = float(total)  * float(0.2)    
    # total = sum(sub.price * sub.quantity for sub in order_details)
    context = {
        'order': order,
        'order_details': order_details,
        'total': total,
        'commissions': commissions,
    }
    return render(request, 'order_details.html', context)       


def commission(request,id):
    customer = get_object_or_404(CustomUser, id=id)
    order = Order.objects.filter(coustmerId_owner_of_prodect=customer.pk) 
    total_commission = order.aggregate(Sum('commission'))
   
    context = {
        'customer': customer,
        'order': order,
        'total_commission': total_commission,
    }    
    return render(request, 'commission.html', context)       




def manage_order(request):
    savaUser=request.user
    user_id=savaUser.id
    orders = Order.objects.all()

    return render(request,'manage_order.html',{"manageOrders":orders})    



def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
       status_up = changeOrderStatus(request.POST, request.FILES, instance=order)
       if status_up.is_valid():
           status_up.save()
           return redirect('/task')
    else:
        status_up = changeOrderStatus(instance=order)
    context = {
        'form':status_up,
    }
    return render(request, 'update_order_status.html',context ={'form': status_up})




def orders_view(request):
    client=request.GET['order_coustmerId']
    print(client)
    orders = Order.objects.all().values('order_number', 'customer_name', 'total_amount', 'commission')
    order_details = OrderDetails.objects.all().values('order__order_number', 'product_name', 'quantity', 'price')
    context = {
        'orders': orders,
        'order_details': order_details,
    }
    return render(request, 'orders.html', context)

