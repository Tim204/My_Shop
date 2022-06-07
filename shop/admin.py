from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Category, Product
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'products_count', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['title']
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.category_thumbnail.name != '':
            return format_html(f'<img src="{instance.category_thumbnail.url}" class="thumbnail" />')
        return ''
    
    # Adding computed fields to see the number of products in each category
    @admin.display(ordering='products_count')
    def products_count(self, category):
        url = (
            # reverse('admin:app-name_model-name_changelist')
            reverse('admin:shop_product_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            }))
        return format_html('<a href="{}">{}</a>', url, str(category.products_count) + " "+'items')
         
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )
    
    class Media:
        css = {
            'all': ['shop/styles.css']
        }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price',
                    'available', 'created', 'updated']
   

    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ['category']
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''
    
    class Media:
        css = {
            'all': ['shop/styles.css']
        }

