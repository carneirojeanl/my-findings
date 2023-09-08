import sys
import os
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from .utils import pil_image_to_django_file


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        product_id = self.request.query_params.get('product_id', None)

        if product_id:
            queryset = queryset.filter(pk=product_id)

        return queryset

    def perform_create(self, serializer):
        picture_name = self.request.data.get('picture_name', None)
        if picture_name:
            new_pic = pil_image_to_django_file(picture_name)
            serializer.save(picture=new_pic)
        else:
            serializer.save()

    def perform_update(self, serializer):
        picture_name = self.request.data.get('picture_name', None)
        if picture_name:
            new_pic = pil_image_to_django_file(picture_name)
            serializer.save(picture=new_pic)
        else:
            serializer.save()
