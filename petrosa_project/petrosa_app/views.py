from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
def products(request):
    return render(request, 'products.html')
def cables(request):
    return render(request, 'cables.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')