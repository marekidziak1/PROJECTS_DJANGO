from .models import Product
from .forms import ProductCreateForm, ProductRawForm
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.urls import reverse

def product_list_view(request):
    queryset = get_list_or_404(Product)
    context={
        'object_list':queryset
    }
    return render(request, "products/product_list.html", context)

def product_detail_view(request, my_id):
    obj1 = get_object_or_404(Product, id=my_id)
    #obj2 = get_object_or_404(Product, id=my_id+1)
    context={
        'object':obj1,
       # 'another_object':obj2,
    }
    #obj1 = Product.objects.get(id=my_id)
    #obj2 = Product.objects.get(id=my_id+1)
    '''
    try:
        obj1 = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    '''
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    if request.method != 'POST':
        initial_Data={'title':'awesom title'}
        form_empty = ProductCreateForm(initial=initial_Data)
        return render(request, "products/product_create.html",{'form':form_empty})
    else:       #if request.method =='POST':
        form_with_data = ProductCreateForm(request.POST)
        if form_with_data.is_valid():
            form_with_data.save()
            return redirect(reverse("products:product_detail", kwargs={'my_id':form_with_data.instance.id}))
        else:
            return render(request, "products/product_create.html",{'form':form_with_data})

def product_delete_view(request, my_id):
    ''' #USUWANIE POPRZEZ GET REQUEST (tylko poprzez link bez strony html)
    obj = get_object_or_404(Product, id=my_id)
    obj.delete()
    return redirect("home")
    '''
    obj = get_object_or_404(Product, id=my_id)
    if request.method != 'POST':
        context ={
            "object":obj
        }
        return render(request, "products/product_delete.html", context)
    else:   #if request.method == 'POST'
        obj.delete()
        return redirect("home")

def product_update_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    if request.method != 'POST':
        form_with_updated_data = ProductCreateForm(instance=obj)
        return render(request, "products/product_create.html",{'form':form_with_updated_data})
    else:       #if request.method =='POST':
        form_with_data = ProductCreateForm(request.POST, instance=obj)
        if form_with_data.is_valid():
            form_with_data.save()
            context={
                'object':obj,
                'another_object':Product.objects.get(id=obj.id)
            }
            #return render(request, "products/product_detail.html",context)
            return redirect(reverse("products:product_detail", kwargs={'my_id':obj.id}))
        else:
            return render(request, "products/product_create.html",{'form':form_with_data})


    
'''=================================================================================='''
def product_create_raw_view(request):
    my_form=None 
    if request.method != 'POST':
        my_form=ProductRawForm()
    else:
        my_form=ProductRawForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
            #print(my_form.cleaned_data.get('title'))
            #print(my_form.errors)
    return render(request, "products/product_create.html",{'form':my_form})


def product_basic_form_view(request):
    context={}
    return render(request, "products/basic_form.html",context)