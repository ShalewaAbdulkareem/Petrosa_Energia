from django.urls import path
from petrosa_app import views




app_name = 'petrosa_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('diesel_generator/', views.diesel_generator, name='diesel_generator'),
    path('gas_generator/', views.gas_generator, name='gas_generator'),
    path('drives/', views.drives, name='drives'),
    path('electrical_panels/', views.electrical_panels, name='electrical_panels'),
    path('kv_panels/', views.kv_panels, name='kv_panels'),
    path('led_light/', views.led_light, name='led_light'),
    path('spare_part/', views.spare_part, name='spare_part'),
    path('transformer/', views.transformer, name='transformer'),
    path('cables/', views.cables, name='cables'),
    path('products/', views.products, name='products'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),

]