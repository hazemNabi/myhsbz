from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser,employees
# from account.forms import addCoustmer,changeOrderStatus,proFiel
# from .models import CoustemSections,Order,Orders,OrderCoustmer,OrderDetails,employees,OrderDetail
from django.db.models import Count

# Create your views here.
from django.contrib.auth.decorators import login_required

from account.forms import CustomUserCreationForm, addCoustmer,addEmployee,EemployeeCreationForm,proFiel
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.db.models import Sum
from order.models import Order


# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('addclient')
#     template_name = 'add_client.html'






@login_required 
def dashboard(request):
        savaUser=request.user
        user_id=savaUser.id
        coust=CustomUser.objects.get(id=user_id)
        # coustem=CustomUser.objects.filter(id=coust)
        print('user id ='+ str(user_id))
        return render(request,'test.html', {'coust':coust})


# from django.db.models.signals import pre_save

# class Order(models.Model):
#     # حقول النموذج
#     assign_employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
#     # باقي الحقول

# @receiver(pre_save, sender=Order)
# def set_assign_employee(sender, instance, **kwargs):
#     if not instance.assign_employee:
#         employee = Employee.objects.filter(emp_company=instance.company, is_busy=False).first()
#         if employee:
#             employee.is_busy = True
#             employee.save()
#             instance.assign_employee = employee

# def assign_employee(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     employee = Employee.objects.filter(emp_company=order.company, is_busy=False).first()
#     if employee:
#         employee.is_busy = True
#         employee.save()
#         order.assign_employee = employee
#         order.save()
#         messages.success(request, f'Task assigned to {employee.name}')
#     else:
#         messages.error(request, 'No available employees')
#     return redirect('order_detail', order_id=order_id)

# from channels.layers import get_channel_layer
# def send_notification(request):
#     new_orders = Order.objects.filter(displayed=False)
#     for order in new_orders:
#         data = {
#             'type': 'notification',
#             'text': f'New order from {order.customer_name} - {order.created_at}',
#         }
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)('new_orders', {'data': data})
#         order.displayed = True
#         order.save()
#     return HttpResponse('Notifications sent.')

def add_client(request):
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
               form.save()
            #    username = form.cleaned_data.get('username')
            #    PhonNumber = form.cleaned_data.get('PhonNumber')
            #    email = form.cleaned_data.get('email')
            #    TypeUser = form.cleaned_data.get('TypeUser')
               return redirect('/dashboard')
                # user.set_password(user.password)
                # user.save()

        return render(request,'add_client.html',{"form":form})

def add_employee(request):
    savaUser=request.user
    user_id=savaUser.id
    coustmer =CustomUser.objects.get(id=user_id)
    Form=EemployeeCreationForm()
    if request.method == 'POST':
       form=EemployeeCreationForm(request.POST,request.FILES)
       if form.is_valid():
        dataform=form.save(commit=False)
        dataform.emp_company=coustmer.pk
        dataform.save()
        return redirect('/manage_employees')
       else:
          dataForm=EemployeeCreationForm()
    return render(request,'add_employee.html',{'form':Form,})

def ProFiel(request):
    savaUser=request.user
    user_id=savaUser.id
    proFiels = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        pro_save = proFiel(request.POST, request.FILES, instance=proFiels)
        if pro_save.is_valid():
           pro_save.save()
           return redirect('/dashboard')
    else:
        pro_save = proFiel(instance=proFiels)
    context = {
        'form':pro_save,
    }
    return render(request,'proFiel.html',context={'form':pro_save})

    # context = {
    #     'proFiel':proFiel,
    # }
    # return render(request,'proFiel.html',context = {"profiel":proFiel})     

def update_client(request,id):
    client =CustomUser.objects.get(id=id)
    if request.method == 'POST':
        client_up = EemployeeCreationForm(request.POST, request.FILES, instance=client)
        if client_up.is_valid():
           client_up.save()
           return redirect('/manage_employees')
    else:
        client_up =   EemployeeCreationForm(instance=client)
    context = {
        'form': client_up,
    }     
    return render(request,'update_client.html',context={'form':client_up})






def user_type_summary(request):
    user_type_summary = CustomUser.objects.values('TypeUser').annotate(total_users=Count('id')).order_by('-total_users')
    return render(request, 'user_type_summary.html', {'user_type_summary': user_type_summary})

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



def manage_client(request):
    savaUser=request.user
    user_id=savaUser.id
    coustomer = CustomUser.objects.all()
    # coustomer = CustomUser.objects.filter(Coustmer_id=user_id)

    return render(request,'manage_client.html',{"coustomer":coustomer})





 



def add_coustmer(request):
    # postData = request.POST
    # username = request.POST.get('username')
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # TypeUser = request.POST.get('TypeUser')
    # form=addCoustmer()
    #         # dataform.set_password(dataform.password)
    #         # dataform.save()
    #         return redirect('manage_client')
    #      else:
    #         print("eeeeeeeeeeeeeeesdasdadacdwscfdwc")
    # else:
    #     print("eeeeeeeeeeeeeee44444444")
    #     form=addCoustmer()

    if request.method == 'POST':
        dataform = addCoustmer(request.POST)
        if dataform.is_valid():
            dataform.save()

    return render(request,'add_customer.html',{"addCoustmer":addCoustmer})





def edit_employee(request, id):
    emp_id = employees.objects.get(id=id)
    if request.method == 'POST':
        emp_up = addEmployee(request.POST, request.FILES, instance=emp_id)
        if emp_up.is_valid():
           emp_up.save()
           return redirect('/manage_employees')

    else:
        emp_up = addEmployee(instance=emp_id)
    context = {
        'form':emp_up,
    }
    return render(request,'edit_employee.html',context={'form':emp_up})

def manage_employees(request):
    savaUser=request.user
    user_id =savaUser.id
    manageEmployees = CustomUser.objects.filter(emp_company=user_id)
    return render(request,'manage_employees.html',{"manageEmployees":manageEmployees})             

def delete_object(request, object_id):
    object = employees.objects.get(id=object_id)
    if request.method == 'POST':
        object.delete()
        messages.success(request, 'Object has been deleted.')
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'manage_employees.html', {'object': object})





def assign_employee(request, task_id):
    task = Order.objects.get(id=task_id)
    employee = CustomUser.objects.filter(emp_company=task.order_coustmerId, is_busy=False).first()
    if employee:
        employee.is_busy = True
        employee.save()
        # task.delivery_Employe = employee
        task.order_status = 'assigned'
        task.save()
        return redirect('manage_order')
    else:
        messages.error(request, 'No available employees')
        return redirect('/manage_order')

def complete_task(request, task_id):
    task = Order.objects.get(id=task_id)
    task.order_status = 'completed'
    # task.delivery_Employe.is_busy = False
    # task.delivery_Employe.save()
    # task.delivery_Employe = None
    task.save()
    return redirect('task_list')

def task(request):   
    savaUser=request.user
    user_id=savaUser.id
    tasks = Order.objects.filter(delivery_Employe=user_id)

    return render(request,'task.html',{"tasks":tasks})   

def accounts(request):
    customer = CustomUser.objects.filter(Q(TypeUser = 1) | Q(TypeUser = 2))

    # total = 0
    # for sub in company:
    #     total += sub.TypeUser
    # context = {
    #     'total':total,
    # }    
    return render(request, 'home.html', {'customer': customer})  