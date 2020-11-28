from rest_framework import generics, filters
from app.models import Producto
from apis.serializer import ProductoSerializer

class ProductoAPIView(generics.ListCreateAPIView):

    filter_backends = (filters.SearchFilter,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
