from django.contrib import admin
from . import models
# Register your models here.

class Product_category_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Product_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(models.Product_category, Product_category_admin)
admin.site.register(models.Product, Product_admin)