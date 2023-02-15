from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Product, Order, Customer, OrderItem, ShippingAddress
from .forms import ProductForm, OrderItemForm, CustomerForm, shippingAddressForm
from .forms import ContactForm
from django.core.mail import send_mail, get_connection
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from onshop.forms import QuoteUserRegistrationForm
from django.contrib.auth.forms import UserChangeForm
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'onshop/products.html', context)

def contact(request):
	submitted = False 
	if request.method == 'POST':
		form = ContactForm(request.POST)
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
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form' : form,
		'page_list' : Customer.objects.all(),
		'submitted' : submitted
	}
	return render(request, 'onshop/contact.html', context)
class ProductDetail(DetailView):
	model = Product
	context_object_name = 'product' #default -> object

	def get_context_data(self, **kwargs):
		context = super(ProductDetail, self).get_context_data(**kwargs)
		context['page_list'] = Product.objects.all()
		return context
class Register(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register-success')

	def get_success_url(self):
		if not self.success_url:
			raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
		return str(self.success_url)  # success_url may be lazy

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.success_url)
class Password_ChangeView(CreateView):
	template_name = 'registration/password_change_form.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register-success')

	def get_success_url(self):
		if not self.success_url:
			raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
		return str(self.success_url)  # success_url may be lazy

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.success_url)

class SearchResultsView(ListView):
    model = Product
    template_name = 'onshop/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list

@login_required(login_url=reverse_lazy('login'))
def product_req(request):
	submitted = False 
	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES)
		if form.is_valid():
			quote = form.save(commit=False)
			try:
				quote.username = request.user
			except Exception:
				pass
			quote.save()
			return HttpResponseRedirect('/quote?submitted=True')
	else:
		form = CustomerForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form' : form,
		'page_list' : Product.objects.all(),
		'submitted' : submitted
	}
	return render(request, 'onshop/quote.html', context)





