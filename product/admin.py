from django.contrib import admin
from product.models import category, Product, Images


class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Images
    Extra = 5

class productAdmin(admin.ModelAdmin):
    list_display = ['title','category','image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]





class imagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','images']



admin.site.register(category,categoryAdmin)
admin.site.register(Product)
admin.site.register(Images,imagesAdmin)