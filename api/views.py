from rest_framework.views import APIView
from sale.models import TypeSale
from .serializer import SaleSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class SaleApiView (APIView):
    def get(self, request, type_sale, material, format=None):
        sale = get_object_or_404(TypeSale,type_sale=type_sale, material=material)
        serialize = SaleSerializer(sale)
        return Response(serialize.data)

class SalePostApiView (APIView):
    def post(self, request, format=None):
        data = request.data
        serialize = SaleSerializer(data=data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return Response(serialize.data,status=201)
        return Response(serialize.errors,status=403)
