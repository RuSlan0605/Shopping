from django.urls import path
from .views import product_list
from .views import contact

urlpatterns = [
	path('', product_list, name='product'),
	path('contact/', contact, name='contact'),
	path('product/', product_list, name='product'),
]
