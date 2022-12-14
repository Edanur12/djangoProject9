from django.contrib import admin
from product.models import category, Product, Images, Comment


class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Images
    Extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}






class imagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ('image_tag',)

class commentAdmin(admin.ModelAdmin):
    list_display = ['subject','status']
    list_filter = ['status']


admin.site.register(category,categoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,imagesAdmin)
admin.site.register(Comment,commentAdmin)