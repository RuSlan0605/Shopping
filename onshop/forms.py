from django import forms
from .models import Customer, Order, OrderItem, Product, ShippingAddress
from django.contrib.auth.forms import UserCreationForm

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

class ContactForm(forms.Form):
	yourname = forms.CharField(max_length=100, label='Your name')
	email = forms.EmailField(required=False, label='Your email')
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea) #textfield

class QuoteUserRegistrationForm(UserCreationForm):

	error_messages = 'Пароли не совпадают!'
