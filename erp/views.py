from django.shortcuts import render
from .models import products


def Home(request):
    return render(request, "erp/home.html")


def ProductsList(request):
    prodsAct = products.objects.filter(Status=1)
    return render(request, "erp/products.html", {"productsActivate": prodsAct})


def NewProduct(request):
    return render(request, "erp/popNewProduct.html")
