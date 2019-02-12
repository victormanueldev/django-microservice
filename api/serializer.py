from rest_framework import serializers
from sale.models import TypeSale

class SaleSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeSale
        fields = '__all__'