from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'in_stock', 'description']
    list_filter = ['in_stock', 'title', 'id_product']
    list_editable = ['price', 'description', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}