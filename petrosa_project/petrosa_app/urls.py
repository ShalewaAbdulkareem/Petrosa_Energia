from django.urls import path
from petrosa_app import views




app_name = 'petrosa_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('project_details/', views.project_details, name='project_details'),

]