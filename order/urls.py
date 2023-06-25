
from django.urls import path
from order.views import orders_view,order_status,details,manage_order
from order import views

urlpatterns = [
    path('orders_view/', views.orders_view, name='orders_view'),
    path('order_status/<int:order_id>', order_status, name='order_status'),
    path('manage_order/', views.manage_order,name='manage_order'),
    # path('delete_object/<int:object_id>',delete_object,name='delete_object'),
    path('details/<int:id>', views.details, name='details'),
]