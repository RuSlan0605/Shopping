from django.contrib import admin
from .models import Customer
from .models import Product
from .models import Order
from .models import OrderItem
from .models import ShippingAddress
from .models import Category

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    ordering = ('price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

