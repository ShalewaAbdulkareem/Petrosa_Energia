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
def diesel_generator(request):
    return render(request, 'diesel_generator.html')
def gas_generator(request):
    return render(request, 'gas_generator.html')
def electrical_panels(request):
    return render(request, 'electrical_panels.html')
def drives(request):
    return render(request, 'drives.html')
def kv_panels(request):
    return render(request, 'kv_panels.html')
def led_lights(request):
    return render(request, 'led_lights.html')
def spare_part(request):
    return render(request,'spare_part.html')
def transformer(request):
    return render(request, 'transformer.html')
def cables(request):
    return render(request, 'cables.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')