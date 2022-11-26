from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from home.models import Brand, Category, New, Product
from home.serializers import BrandSerializer, CategorySerializer, NewSerializer, ProductSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Welcome to the Django Api")


@api_view(["GET", "POST"])
def brand_list(request, format=None):

    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def brand_details(request, id, format=None):
    try:
        brand = Brand.objects.get(id=id)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({"products": serializer.data})


@api_view(["GET", "DELETE"])
def product_details(request, id):
    try:
        product = Product.objects.get(id=id)

    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({"category": serializer.data})


@api_view(["GET", "DELETE"])
def category_details(request, id):
    try:
        category = Category.objects.get(id=id)
    except category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def news_list(request):
    if request.method == "GET":
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return JsonResponse({"category": serializer.data})


@api_view(["GET", "DELETE"])
def news_details(request, id):
    try:
        new = New.objects.get(id=id)
    except new.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewSerializer(new)
        return Response(serializer.data)
    elif request.method == "DELETE":
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
