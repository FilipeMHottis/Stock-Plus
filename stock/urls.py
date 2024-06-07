from .views import (
    login,
    products,
    product_create,
    tag_create,
    category_create,
)
from django.urls import path

urlpatterns = [
    path("login/", login, name="login"),
    path("products/", products, name="products"),
    path("product_create/", product_create, name="product_create"),
    path("tag_create/", tag_create, name="tag_create"),
    path("category_create/", category_create, name="category_create"),
]
