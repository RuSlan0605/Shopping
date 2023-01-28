from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Product
from .models import Order
from .models import Customer
from .forms import ProductForm
from .forms import OrderForm
from django.core.mail import send_mail, get_connection


def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'onshop/products.html', context)

def contact(request):
	submitted = False 
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['pythonDevCRM.pythonanywhere.com'],
				connection = con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ProductForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form' : form,
		'page_list' : Product.objects.all(),
		'submitted' : submitted
	}
	return render(request, 'onshop/contact.html', context)





