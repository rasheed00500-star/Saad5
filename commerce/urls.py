from django.urls import path
from .views import home
from django.urls import path
from .views import home, products_view


urlpatterns = [
    path('', home, name='commerce-home'),
]


urlpatterns = [
    path('', home, name='commerce-home'),
    path('products/', products_view, name='products'),
]
