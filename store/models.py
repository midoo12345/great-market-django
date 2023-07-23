from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=100,blank=True)
    cat_image = models.ImageField(upload_to='images/category',blank=True)
    
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
            return reverse('products_by_category', args=[self.slug])
        
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField( upload_to='images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
            return reverse('product_detail', args=[self.category.slug,self.slug])
    
    
    def __str__(self):
        return self.product_name
    
    