from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone
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