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
    selected_category = None
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        selected_category = category.name
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories, 'selected_category': selected_category})




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
    products = TrueValueProduct.objects.all()
    return render(request, 'truevalue.html', {'products': products})

def truevalue_product_detail(request, slug):
    product = get_object_or_404(TrueValueProduct, slug=slug)
    return render(request, 'truevalue-details.html', {'product': product})

def quick_quote(request, product_slug):
    product = get_object_or_404(TrueValueProduct, slug=product_slug)  # Get product by slug

    if request.method == 'POST':
        form = QuickQuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.product = product  
            quote.save()
            messages.success(request, "Your quote request has been submitted successfully!")
            return redirect(product.get_absolute_url())  
        else:
            messages.error(request, "There was an error submitting the form. Please try again.")
    else:
        form = QuickQuoteForm(initial={'product': product.name})  

    return render(request, 'quick-quote.html', {'form': form, 'product': product})