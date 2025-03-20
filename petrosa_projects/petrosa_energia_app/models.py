# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify  # ✅ Import slugify
# from django.utils.timezone import now



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name

    def has_subcategories(self):
        return self.subcategories.exists()

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, verbose_name='Product Name')
    slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='product_images/')
    in_stock = models.BooleanField(default=True)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['slug', 'category']),
        ]
        
    def show_image1(self):
        if self.image:
         return self.image.url

class ProductInterest(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255,null=True,blank=True)
    company_name =models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=False, verbose_name="Phone No")
    message = HTMLField()
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Add slug field
    created_at = models.DateTimeField(default =timezone.now)
    def __str__(self):
        return f'Interest in {self.product.product_name} by {self.name}'

    def show_image1(self):
        if self.image:
            return self.image.url
        
    def __str__(self): 
        return self.product_name   
    
    def get_absolute_url(self):
        return reverse('petrosa_energia_app:product_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # ✅ Generate a slug if missing
        super().save(*args, **kwargs)




class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to = 'services/')
    name = models.CharField(max_length=200)
    content = HTMLField()

    def __str__(self):
        return self.name
        
class Project_name(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'projects/')

    def __str__(self):
        return self.name
    
    

class TrueValueProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)
    description = HTMLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='truevalue_products/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'TrueValue'
        ordering = ('-created_at',)


    def show_image1(self):
        if self.image:
            return self.image.url   
    
    def get_absolute_url(self):
        return reverse('petrosa_energia_app:true_product_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Use timezone.now for default


class QuickQuote(models.Model):
    product = models.ForeignKey(TrueValueProduct, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True, null=True)
    company_address =models.TextField(null=True, blank=True) 
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote from {self.first_name} {self.last_name}"
