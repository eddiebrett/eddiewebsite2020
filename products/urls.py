from django.conf.urls import url, include
from .views import all_products

app_name = "shop"

urlpatterns = [
    url(r'^$', all_products, name='products'),
]

