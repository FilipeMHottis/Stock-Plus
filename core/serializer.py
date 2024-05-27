from rest_framework import serializers
from .models import Product, Tag, Category


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
