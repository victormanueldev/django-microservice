from djongo import models

# Create your models here.
class TypeSale (models.Model):
    material = models.CharField(max_length=255,null=True)
    type_sale = models.CharField(max_length=255,null=True)
    ean = models.CharField(max_length=255,null=True)
    ppsi = models.FloatField(null=True)
    objects = models.DjongoManager()