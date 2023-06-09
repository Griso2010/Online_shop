from django.urls import path
from products.views import products, basket_add, basket_remove


urlpatterns = [
    path('', products, name='products'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_remove/<int:basket_id>/', basket_remove, name='basket_remove'),

]

