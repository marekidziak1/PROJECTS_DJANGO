from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product, Order, Customer
from .forms import OrderForm
from django.forms import inlineformset_factory
from . filters import OrderFilter
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context={'orders': orders, 'customers': customers, 'total_cutomers':total_customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accounts/dashboard.html', context)
def contact(request):
    context={}
    return render(request, 'accounts/contact.html', context)
def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'accounts/products.html', context)
def customer(request, pk):
    try:
        customer= Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return redirect('customer_blank')
    else:
        orders = customer.order_set.all()
        myFilter = OrderFilter(request.GET, queryset=orders)
        orders = myFilter.qs
    context={'orders': orders, 'customer': customer, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

'''
def createOrder(request,pk):
    customer = Customer.objects.get(id=pk) 
    form =OrderForm()
    #form =OrderForm(initial={'customer':customer})
    if request.method =='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer
            order.save()
            return HttpResponseRedirect(reverse('home'))
    context={'form':form, 'customer':customer}
    return render(request, 'accounts/order_form.html', context)
'''

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=10)
    customer = Customer.objects.get(id=pk) 
    formset = OrderFormSet(instance=customer)
    if request.method =='POST':
        formset=OrderFormSet(request.POST, queryset=Order.objects.none(), Orderinstance=customer )
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('home'))
    context={'formset':formset, 'customer':customer}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    form =OrderForm(instance =order)
    if request.method =='POST':
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context={'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    if request.method =='POST':
        order.delete()
        return HttpResponseRedirect(reverse('home'))
    context={}
    return render(request, 'accounts/delete.html', context)
    