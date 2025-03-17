from django.contrib import admin
from petrosa_app.models import *
from django.utils.text import slugify

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent') 
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',) 
    list_filter = ('name',)  

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'in_stock', 'created_at')  
    list_filter = ('category', 'in_stock')  
    search_fields = ('product_name', 'category__name')  
    prepopulated_fields = {'slug': ('product_name',)}  
    ordering = ('-created_at',)  

admin.site.register(Product, ProductAdmin)

@admin.register(ProductInterest)
class ProductInterestAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'company_name','phone_number','product', 'created_at')
    search_fields =('name', 'email', 'product')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'email','product__product_name')

@admin.register(Service)
class ServiceAmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project_name)
class Project_nameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    

class TrueValueProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'uploaded_at')  
    list_filter = ('created_at', 'uploaded_at')
    prepopulated_fields = {'slug': ('name',)}  
    ordering = ('-created_at',) 

admin.site.register(TrueValueProduct, TrueValueProductAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
