from django.contrib import admin
from .models import Subscriber
from .models import Product
from .models import Testimonial

admin.site.register(Subscriber)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'testimonial', 'created_at')    
# Register your models here.
