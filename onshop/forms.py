from django import forms
from .models import Customer, Order, OrderItem, Product, ShippingAddress

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('__all__')

class shippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('__all__')    
