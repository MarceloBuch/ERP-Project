from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import products
from django.urls import reverse_lazy


def Home(request):
    return render(request, "erp/home.html")


class ProductListView(ListView):
    model = products


class ProductsCreateView(CreateView):
    model = products
    fields = ["Cod", "Desc", "Cod_Barra", "Unit_Cost", "Sale_Price"]
    success_url = reverse_lazy("ProductsList")

    def form_valid(self, form):
        form.instance.Status = 1
        return super().form_valid(form)
