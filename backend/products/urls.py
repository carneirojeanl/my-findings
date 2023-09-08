from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from .views import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls


