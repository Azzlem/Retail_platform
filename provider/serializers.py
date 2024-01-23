from rest_framework import serializers
from products.serializers import ProductSerializer
from provider.models import Provider


class RetailSerializerView(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)

    class Meta:
        model = Provider
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class ProviderSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Provider
        exclude = ['debt']


