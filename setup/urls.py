from django.contrib import admin
from django.urls import path
from erp.views import ProductsList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProductsList),
]
