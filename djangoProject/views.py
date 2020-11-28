from django.shortcuts import render
from rest_framework import generics, filters
from app.models import Producto
from apis.serializer import ProductoSerializer

class ProductoAPIView(generics.ListCreateAPIView):
    search_fields=['nombre','precio']
    filter_backends = (filters.SearchFilter,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class DetalleProducto(generics.RetrieveUpdateDestroyAPIView):
    queryset=Producto.objects.all()
    serializer_class = ProductoSerializer