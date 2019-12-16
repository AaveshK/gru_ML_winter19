from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

#rest_framework imports
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

#app level imports
from ecom.models import Product
from ecom.models import Clothing
from ecom.models import Electronics
from ecom.models import Books
from ecom.models import Sports
from ecom.models import Kitchen
from ecom.serializers import ProductSerializer
from ecom.serializers import ClothingSerializer
from ecom.serializers import ElectronicsSerializer
from ecom.serializers import BooksSerializer
from ecom.serializers import SportsSerializer
from ecom.serializers import KitchenSerializer

# Create your views here.
@csrf_exempt
def func_view(request):
    if request.method == 'GET':
        #some code logic
        #return render(request, 'ecom/head.html')
        return HttpResponse("OK")
    elif request.method == 'POST':
        #some code logic
        return HttpResponse(request.body)

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['GET'], detail=False,url_path="budget")
    def budget(self, request):
        budget = Product.objects.filter(price__lte=5000)
        serializer = ProductSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False,url_path="costly")
    def costly(self, request):
        costly = Product.objects.filter(price__gte=5000)
        serializer = ProductSerializer(costly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClothingView(viewsets.ModelViewSet):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

    @action(methods=['GET'], detail=False,url_path="budget")
    def budget(self, request):
        budget = Clothing.objects.filter(price__lte=1500)
        serializer = ClothingSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False,url_path="costly")
    def costly(self, request):
        costly = Clothing.objects.filter(price__gte=5000)
        serializer = ClothingSerializer(costly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SportsView(viewsets.ModelViewSet):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer

    @action(methods=['GET'], detail=False,url_path="budget")
    def budget(self, request):
        budget = Sports.objects.filter(price__lte=1500)
        serializer = SportsSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False,url_path="costly")
    def costly(self, request):
        costly = Sports.objects.filter(price__gte=5000)
        serializer = SportsSerializer(costly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KitchenView(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer

    @action(methods=['GET'], detail=False,url_path="budget")
    def budget(self, request):
        budget = Kitchen.objects.filter(price__lte=1500)
        serializer = KitchenSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False,url_path="costly")
    def costly(self, request):
        costly = Kitchen.objects.filter(price__gte=5000)
        serializer = KitchenSerializer(costly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ElectronicsView(viewsets.ModelViewSet):
    queryset = Electronics.objects.all()
    serializer_class = ElectronicsSerializer

    @action(methods=['GET'], detail=False,url_path="budget")
    def budget(self, request):
        budget = Electronics.objects.filter(price__lte=1500)
        serializer = ElectronicsSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False,url_path="costly")
    def costly(self, request):
        costly = Electronics.objects.filter(price__gte=5000)
        serializer = ElectronicsSerializer(costly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    @action(methods=['GET'], detail=False,url_path="budget")
    def budget(self, request):
        budget = Books.objects.filter(price__lte=1500)
        serializer = BooksSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False,url_path="costly")
    def costly(self, request):
        costly = Books.objects.filter(price__gte=5000)
        serializer = BooksSerializer(costly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)