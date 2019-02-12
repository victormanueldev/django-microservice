from rest_framework.views import APIView
from sale.models import TypeSale
from .serializer import SaleSerializer
from rest_framework.response import Response

class SaleApiView (APIView):
    def get(self, request, type, material, format=None):
        sale = TypeSale.objects.filter(type_sale=type, material=material)
        serialize = SaleSerializer(sale, many=True)
        return Response(serialize.data)
