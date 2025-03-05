from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name

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
        
    def __str__(self): 
        return self.product_name   
    
    def get_absolute_url(self):
        return reverse('petrosa_app:product_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)


class ProductInterest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the Product model
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = HTMLField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Interest in {self.product.product_name} by {self.name}"

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services_images/')  # Change "ImageField" to "image"
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

