from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect ,get_object_or_404
from prodect.models import Products,CoustemSections
# from .forms import ,changeOrderStatus
# from product.models import CoustemSections
from django.db.models import Count

# Create your views here.
from django.contrib.auth.decorators import login_required

from prodect.forms import addProdect,addSections
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.db.models import Sum
from account.models import CustomUser
   
   
def add_prodect(request):
    savaUser=request.user
    user_id=savaUser.id
    coustmer =CustomUser.objects.get(id=user_id)
    Form=addProdect()
    # coustemCatogry=CoustemSections.objects.get(Coustmer_id=user_id)
    # coustemSection1=addSections(data={'Coustmer_id':coustemSection})
    if request.method == 'POST':
       form=addProdect(request.POST,request.FILES)
       if form.is_valid():
        dataform=form.save(commit=False)
        dataform.prodect_CoustmerId=coustmer
        dataform.save()
        return redirect('/manage_prodect')
       else:
          dataForm=addProdect()
    return render(request,'add_prodect.html',{'form':Form,})



def manage_prodect(request):
    savaUser=request.user
    user_id=savaUser.id
    manageProdect = Products.objects.filter(prodect_CoustmerId=user_id)
    return render(request,'manage_prodect.html',{"manageProdect":manageProdect})     

def delete(request, id):
    object = Products.objects.get(id=id)
    if request.method == 'POST':
        object.delete()
        # messages.success(request, 'Object has been deleted.')
        # return redirect(request.META.get('HTTP_REFERER'))
        return redirect('/mange_prodect')
    return render(request, 'delete.html', {'object': object})

def remov_section(request, id):
    object = CoustemSections.objects.get(id=id)
    if request.method == 'POST':
        object.delete()
        # messages.success(request, 'Object has been deleted.')
        # return redirect(request.META.get('HTTP_REFERER'))
        return redirect('/manage_sections')
    return render(request, 'delete_section.html', {'object': object})


def update_product(request, id):
    product_id = Products.objects.get(id=id)
    if request.method == 'POST':
        product_save = addProdect(request.POST, request.FILES, instance=product_id)
        if product_save.is_valid():
           product_save.save()
           return redirect('/manage_prodect')
    else:
        product_save = addProdect(instance=product_id)
    context = {
        'form':product_save,
    }
    return render(request,'update_product.html',context={'form':product_save})


def show_product(request,id):
    product_id = Products.objects.get(id=id)
    if request.method == 'POST':
        product_save = addProdect(request.POST, request.FILES, instance=product_id)
        if product_save.is_valid():
           product_save.save()
           return redirect('/manage_prodect')
    else:
        product_save = addProdect(instance=product_id)
    context = {
        'form':product_save,
    }
    return render(request,'show_product.html',context={'form':product_save})




# def commission(request,id):
#     customer = get_object_or_404(CustomUser, id=id)
#     order = Order.objects.filter(coustmerId_owner_of_prodect=customer.id) 
#     total_commission = order.aggregate(Sum('commission'))
   
#     context = {
#         'customer': customer,
#         'order': order,
#         'total_commission': total_commission,
#     }    
#     return render(request, 'commission.html', context)

def update_section(request, id):
    section_id = CoustemSections.objects.get(id=id)
    if request.method == 'POST':
        section_up = addSections(request.POST, request.FILES, instance=section_id)
        if section_up.is_valid():
           section_up.save()
           return redirect('/manage_sections')

    else:
        section_up = addSections(instance=section_id)
    context = {
        'form':section_up,
    }
    return render(request,'update_section.html',context={'form':section_up})


def manage_sections(request):
    savaUser=request.user
    user_id=savaUser.id
    coustemSections = CoustemSections.objects.filter(Coustmer_id=user_id)
    return render(request,'manage_sections.html',{"coustemSections":coustemSections})

def add_sections(request):
    savaUser=request.user
    user_id=savaUser.id
    coustmer =CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
       dataForm= addSections(request.POST)
       if dataForm.is_valid():
            dataform=dataForm.save(commit=False)
            dataform.Coustmer_id=coustmer
            dataform.save()
            return redirect('manage_sections')
    else:
        dataForm= addSections()
    return render(request,'add_sections.html',{'form':addSections()})
