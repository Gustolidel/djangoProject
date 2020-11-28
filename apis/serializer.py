
from rest_framework import serializers
from app.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'
