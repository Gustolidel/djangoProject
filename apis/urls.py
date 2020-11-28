from django.urls import path
from djangoProject.views import ProductoAPIView,DetalleProducto

urlpatterns=[
path('',ProductoAPIView.as_view()),
    path('<int:pk>/',DetalleProducto.as_view())
]