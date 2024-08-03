from django.db import models


class products(models.Model):
    Cod = models.CharField(max_length=244, null=False, blank=False)
    Desc = models.CharField(max_length=244, null=False, blank=False)
    Cod_Barra = models.CharField(max_length=299)
    Status = models.IntegerField(null=False, blank=False)
    Date_Create = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    Unit_Cost = models.FloatField(null=False, blank=False)
    Sale_Price = models.FloatField(null=False, blank=False)
