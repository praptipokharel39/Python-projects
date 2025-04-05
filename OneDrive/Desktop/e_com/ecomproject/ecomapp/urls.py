from django.urls import path
from .views import *



app_name = "ecomapp"

urlpatterns =[
    path("", HomeView.as_view() , name = "home"),
    path('cart/<int:pro_id>/',AddtoCart.as_view(), name="cart"),
    path('Category/',AllProducts.as_view(), name="category"),
    path("productdetails/<slug:slug>/", AboutProducts.as_view(), name="productdetails"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCart.as_view(), name="managecart"),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("customer/", Customer.as_view(), name="customer"),


    
]
