from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ecom.models import Setting,ContactForm,ContactMessage
from product.models import Product,Images,Category
from ecom.forms import SearchForm
from oderapp.models import ShopCart

def home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price * p.quantity
    product_catagory=Category.objects.all()
    setting=Setting.objects.get(id=1)
    slide_img=Product.objects.all().order_by('id')[:2]
    lasted_product=Product.objects.all().order_by('-id')
    products=Product.objects.all()
    context={'setting':setting,
         'slide_img':slide_img,
         'lasted_product':lasted_product,
         'products':products,
        'product_catagory':product_catagory,
        'total_amount':total_amount,
        'cart_product':cart_product
         }
    return render(request,'home.html',context)

def about(request):
    product_catagory = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={
        'setting': setting,
        'product_catagory': product_catagory,
    }
    return render(request,'about.html',context)

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # messages.success(request, 'Profile details updated.')

            return redirect('contact')

    setting = Setting.objects.get(id=1)
    product_catagory = Category.objects.all()
    form = ContactForm

    context = {
        'form': form,
        'setting':setting,
        'product_catagory': product_catagory,
    }
    return render(request, 'contact.html', context)




def product_single(request,id):
    product_catagory = Category.objects.all()
    setting = Setting.objects.get(id=1)
    single_product =Product.objects.get(id=id)
    image = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:3]
    contex={
        'product_catagory': product_catagory,
        'setting':setting,
        'single_product':single_product,
        'image':image,
        'products': products,
            }
    return render(request,'single_product.html',contex)


def category_product(request,id,slug):
    product_catagory = Category.objects.all()
    setting = Setting.objects.get(id=1)
    product_cat=Product.objects.filter(category_id=id)
    slide_img = Product.objects.all().order_by('id')[:2]
    context={
        'product_cat':product_cat,
        'setting':setting,
        'product_catagory': product_catagory,
        'slide_img': slide_img,
    }
    return render(request,'category_product.html',context)



def SearchView(request):
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            product_catagory = Category.objects.all()
            slide_img = Product.objects.all().order_by('id')[:2]
            setting = Setting.objects.get(pk=1)
            context = {
                'product_catagory': product_catagory,
                'query': query,
                'product_cat': products,
                'slide_img': slide_img,
                'setting': setting,
            }
            return render(request, 'category_product.html', context)
        return HttpResponseRedirect('category_product')



