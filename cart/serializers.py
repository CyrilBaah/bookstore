from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    """Serializer for Cart"""

    class Meta:
        model = Cart
        fields = "__all__"
