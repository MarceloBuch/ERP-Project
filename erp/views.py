from django.shortcuts import render
from .models import products

def ProductsList(request):
    prods = products.objects.all()
    return render(request, "erp/products.html", {"products": prods})
