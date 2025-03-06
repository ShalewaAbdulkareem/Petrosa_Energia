from django.contrib import admin
from petrosa_app.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent') 
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',) 
    list_filter = ('name',)  

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category',  'in_stock', 'created_at')  
    list_filter = ('category', 'in_stock')  
    search_fields = ('product_name', 'category__name')  
    prepopulated_fields = {'slug': ('product_name',)}  
    ordering = ('-created_at',)  
admin.site.register(Product, ProductAdmin)


@admin.register(ProductInterest)
class ProductInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created_at')
    search_fields = ('name', 'email', 'product__product_name')
    list_filter = ('created_at',)

<<<<<<< HEAD
=======

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
>>>>>>> 18a42268e80cac33f05c10d251e30d3b96d15231
