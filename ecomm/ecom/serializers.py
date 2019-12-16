from rest_framework import serializers

from ecom.models import Product
from ecom.models import Clothing
from ecom.models import Electronics
from ecom.models import Books
from ecom.models import Sports
from ecom.models import Kitchen

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price']
class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['name','price']
class ElectronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronics
        fields = ['name','price']
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['name','price']
class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = ['name','price']
class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ['name','price']