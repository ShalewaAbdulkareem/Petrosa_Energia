from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from petrosa_app.models import *
from petrosa_app.forms import *
from django.contrib import messages 

# Create your views here.
def index(request):
    brands = Brand.objects.all()
    our_service = Service.objects.all()
    context = {
        'brands': brands,
        'our_service': our_service,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    our_service = Service.objects.all()
    context = {
        'our_service': our_service
    }
    return render(request, 'services.html', context)

def products(request, category_slug=None):
    categories = Category.objects.filter(parent=None).prefetch_related('subcategories')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})




def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = ProductInterestForm(request.POST, product=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your interest in '{product.product_name}' has been submitted successfully! Our Customercare will get in touch with you shortly")
           
            return redirect('petrosa_app:product_detail', slug=slug)
    else:
        form = ProductInterestForm(product=product)

    return render(request, 'product-detail.html', {'product': product, 'form': form})


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')


def project(request):
    all_project = Project_name.objects.all()
    context = {
        'all_project': all_project
    }
    return render(request, 'project.html', context)


def project_details(request):
    return render(request, 'project_details.html')


def truevalue(request):
    return render(request, 'truevalue.html')

def truevalue_detail(request):
    return render(request, 'truevalue-detail.html')