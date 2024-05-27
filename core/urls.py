from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, TagViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("tags", TagViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
