from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


# Create your models here.
class category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(category, on_delete=models.CASCADE)  # category tablosu ile ilişkilendirme
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=300)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

def image_tag(self):
    return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

def __str__(self):
        return self.title

def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})







class Images(models.Model):
    title = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(blank=True, upload_to='images/')

def __str__(self):
        return self.title

def image_tag(self):
    return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

image_tag.short_description='image'


