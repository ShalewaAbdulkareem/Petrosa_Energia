# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from petrosa_energia_app.models import *
from petrosa_energia_app.forms import *
from django.contrib import messages 
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail  # Import send_mail




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
            interest = form.save()

            # Emails of the two recipients
            recipient_emails = [settings.EMAIL_HOST_USER, 'md@petrosaglobal.com']

            # Email Subject and Message
            subject = f"New Product Inquiry: {interest.product.product_name}"
            message = f"""
            A customer has shown interest in {interest.product.product_name}.

            
            Name: {interest.name}
            Email: {interest.email}
            Address: {interest.address}
            Company Name: {interest.company_name}
            Phone Number: {interest.phone_number}
            Message: {interest.message}


            
            """

            # ✅ Send email using send_mail
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_emails)

            messages.success(request, f"Your interest in '{product.product_name}' has been submitted successfully! Our customer care will get in touch with you shortly.")
            return redirect('petrosa_energia_app:product_detail', slug=slug)
    else:
        form = ProductInterestForm(product=product)

    return render(request, 'product-detail.html', {'product': product, 'form':form})

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            messages.error(request, 'Fields cannot be empty')
        else:
            data = Contact(name=name, email=email, subject=subject, message=message)
            email_subject = f'{subject}: FROM PETROSA ENERGIA LTD WEBSITE'
            email_data = {
                'name': name,
                'email': email,
                'message': message
            }
            html_message = render_to_string('contact-mail.html', email_data)
            plain_message = strip_tags(html_message)
            from_email = 'PETROSA ENERGIA LTD<customercare@petrosaglobal.com>'
            recipient_list = [settings.EMAIL_HOST_USER, "md@petrosaglobal.com"]

            try:
                email_message = EmailMessage(email_subject, plain_message, from_email, recipient_list)
                email_message.send()
                data.save()
                messages.success(request, 'Message sent successfully')
            except Exception as e:
                messages.error(request, f'Failed to send message: {str(e)}')

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
    form = QuickQuoteForm(initial={'product': product.name})  # 👈 Always initialize the form

    if request.method == 'POST':
        form = QuickQuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.product = product  
            quote.save()

            # **SEND EMAIL TO CUSTOMER CARE**
            email_subject = f"Quick Quote Request for {product.name}"
            email_data = {
                "product": product.name,
                "first_name": quote.first_name,
                "last_name": quote.last_name,
                "email": quote.email,
                "company": quote.company,
                'company_address': quote.company_address ,
                "phone": quote.phone,
                "message": quote.message,
            }

            html_message = render_to_string("quickquote-mail.html", email_data)
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            try:
                email_message = EmailMessage(email_subject, plain_message, from_email, recipient_list)
                email_message.send()
                messages.success(request, "Your quote request has been submitted successfully!")
            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")

            return redirect(product.get_absolute_url())  
        else:
            messages.error(request, "There was an error submitting the form. Please try again.")

    return render(request, 'quick-quote.html', {'form': form, 'product': product})
