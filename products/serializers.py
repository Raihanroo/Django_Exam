from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_id",
            "name",
            "category",
            "price",
            "quantity",
            "status",
            "last_updated",
        ]
        read_only_fields = ["id", "last_updated"]
