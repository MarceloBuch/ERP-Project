from django.contrib import admin
from django.urls import path
from erp.views import Home, ProductListView, ProductsCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home, name="Home"),
    path("products", ProductListView.as_view(), name="ProductsList"),
    path("NewProduct", ProductsCreateView.as_view(), name="NewProduct"),
]
