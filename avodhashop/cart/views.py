from django.shortcuts import render,redirect,get_object_or_404

import cart
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def cart_details(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quan)
            count +=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

# def cart_details(request,total=0,tax=0,grand_total=0,cart_items=None,product_qty=0):
#     cart_count = 0
#     carts = cart.objects.filter(user=request.user)
#     for item in carts:
#         sub_total = (item.product.mrp * item.product_qty)
#         total += (item.product.mrp * item.product_qty)
#         product_qty += item.product_qty
#         cart_count += product_qty
#         tax = (3 * total)/100
#         grand_total = total + tax
#         context = {'total':total,'product_qty':product_qty,'carts':carts,'tax':tax,'grand_total':grand_total,'sub_total':sub_total,'cart_count':cart_count}
#         return render(request,'store/cart.html',context)





def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

# def add_cart(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             product_check = products.objects.get(id=prod_id)
#             if product_check:
#                 if cart.objects.filter(user=request.user.id,product_id=prod_id):
#                     return JsonResponse({'status':"product already in cart"})
#                 else:
#                     prod_qty = int(request.POST.get('product_qty'))
#                     if product_check.is_available==True:
#                         cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
#                         return JsonResponse({'status':"product added successfully"})
#                     else:
#                         return JsonResponse({'status': 'No such product found'})
#             else:
#                 return JsonResponse({'status': "login to continue"})
#             return redirect('/')
#
#




def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products,id=product_id)
    c_items = items.objects.get(prodt=prod,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')
def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products,id=product_id)
    c_items = items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cartDetails')

