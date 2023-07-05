from django.contrib import admin
from .models import Product, Discount

# Register your models here.


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin): # contructing ProductAdmin class with the base class ModelAdmin from the admin library
    list_display = ('name', 'price', 'stock') # specifies the columns that will be visable in the table


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Product, ProductAdmin)



