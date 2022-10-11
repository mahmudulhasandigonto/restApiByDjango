from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from home.models import Brand, Category
from home.serializers import BrandSerializer, CategorySerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def brand(request, format=None):

    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return JsonResponse({"category": serializer.data})
    else:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

