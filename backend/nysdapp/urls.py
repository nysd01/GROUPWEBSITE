from django.urls import path,include

from . import views

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static



jls_extract_var = views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat,name='chat'),
    path('contact/', views.contact,name='contact'),
    path('login/',jls_extract_var.login_view,name='login'),
    path('service/',views.service,name='service'),
    path('register/',views.register,name='register'),
    path('search/', views.search_view, name='search'),
    path('cart/',views.cart, name='cart'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('reset_cart/', views.reset_cart, name='reset_cart'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
