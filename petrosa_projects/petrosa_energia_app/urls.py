from django.urls import path
from petrosa_energia_app import views




app_name = 'petrosa_energia_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('category/<slug:category_slug>/', views.products, name='products'),  
    path('products/', views.products, name='products'), 
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('project_details/', views.project_details, name='project_details'),
    path('truevalue/', views.truevalue, name='truevalue'),
    path('truevalue/<slug:slug>/', views.truevalue_product_detail, name='true_product_detail'),
    path('quick-quote/<slug:product_slug>/', views.quick_quote, name='quick_quote'),
    path('search/',views.search,name='search'),
]