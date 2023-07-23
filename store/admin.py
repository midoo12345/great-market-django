from django.contrib import admin
from . models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display =('name', 'slug')



admin.site.register(Category,CategoryAdmin,)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('product_name',)}
    list_display =('product_name', 'price','stock','category','is_available','modified_date')

admin.site.register(Product,ProductAdmin)