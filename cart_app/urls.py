from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>', views.add_product, name='add'),
    path('delete/<int:product_id>', views.delete_product, name='delete'),
    path('decrease/<int:product_id>', views.decrease_product, name='decrease'),
    path('clean/<int:product_id>', views.clean_cart, name='clean'),
]