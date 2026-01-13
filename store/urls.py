from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-complete/', views.order_complete, name='order_complete'),
    path('main/', views.main, name='main'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('toggle_wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
]