from django.urls import path
from .views import *

urlpatterns = [
    path('',Index,name='Index'),
    path('About/',About,name='About'),
    path('AddProduct/',AddProduct,name='AddProduct'),
    path('Productdata/',Productdata,name='Productdata'),
    path('Product/',allProduct,name='Product'),
    path('Delete/<int:pk>',Delete,name='Delete'),
    path('AddToCart/<int:pk>',AddToCart,name='AddToCart'),
    path('Cart/',Cart,name='Cart'),
    path('Payment/',Payment,name='Payment'),
    path('payment-status', payment_status, name='payment-status'),
    path('Contact/',Contact,name='Contact'),
    #  path('dashboard/',dashboard,name='dashboard'),
    #  path('cartss',cartss,name='cartss'),
    #  path('addtocart/<int:pk>',addtocart ,name='addtocart'),
    #  path('delete/<int:pk>',delete,name='delete'),
    #  path("payment/",payment,name='payment'),
    #  path('payment-status', payment_status, name='payment-status'),
    #  path('',index,name='Index'),
    #  path('About/',About,name='About'),
    #  path('AddProduct/',AddProduct,name='AddProduct'),
    #  path('Productdata/',Productdata,name='Productdata'),
    #  path('Product/',allProduct,name='Product'),
    #  path('Cart/',Cart,name='Cart'),
    #  path('Contact/',Contact,name='Contact'),
]