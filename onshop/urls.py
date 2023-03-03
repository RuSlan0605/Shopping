from django.urls import path
from .views import product_list, by_category
from .views import contact, product_req
from .views import ProductDetail, SearchResultsView

urlpatterns = [
	path('', product_list, name='product'),
	path('categories/', by_category, name='categories'),
	path('contact/', contact, name='contact'),
	path('product_req/', product_req, name='product-req'),
	path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
	path('search/', SearchResultsView.as_view(), name='search_results'),
]
