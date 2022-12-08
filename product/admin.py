from django.contrib import admin
from product.models import category, Product, Images


class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Images
    Extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]






class imagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ('image_tag',)



admin.site.register(category,categoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,imagesAdmin)