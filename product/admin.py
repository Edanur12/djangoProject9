from django.contrib import admin
from product.models import category
class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
# Register your models here.
admin.site.register(category,categoryAdmin)