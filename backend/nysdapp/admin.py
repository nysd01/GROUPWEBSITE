from django.contrib import admin
from .models import Subscriber
from .models import Product

admin.site.register(Subscriber)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
# Register your models here.
