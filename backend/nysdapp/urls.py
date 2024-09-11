from django.urls import path, include

from . import views

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

#jls_extract_var = views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login_view, name='login'),
    path('service/', views.service, name='service'),
    path('register/', views.register, name='register'),
    path('search/', views.search_view, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('reset_cart/', views.reset_cart, name='reset_cart'),
    path('payment/', views.payment, name='payment'),
    path('service/', views.service_view, name='service_view'),
    path('about/', views.about, name='about'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
