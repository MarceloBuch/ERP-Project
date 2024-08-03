from django.contrib import admin
from django.urls import path
from erp.views import Home, ProductsList, NewProduct

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home, name="Home"),
    path("products", ProductsList, name="ProductsList"),
    path("NewProduct", NewProduct, name="NewProduct"),
]
