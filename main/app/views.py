from rest_framework.generics import ListAPIView
from .models import Product, Warehouse, ProductGroup
from .serializers import ProductSerializer, WarehouseSerializer, ProductGroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': {"message": "Product added"}}, status=status.HTTP_201_CREATED)
    return Response({'error': {'code': 422, 'message': 'Validation error', 'error': serializer.errors}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET', 'PATCH', 'DELETE'])
def detailProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': {'code': 404, 'message': 'Not found'}}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': {'code': 422, 'message': 'Validation error', 'error': serializer.errors}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'data': {'message': 'Product removed'}}, status=status.HTTP_200_OK)


@api_view(['GET'])
def productGroupList(request):
    product_groups = ProductGroup.objects.all()
    serializer = ProductGroupSerializer(product_groups, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def addProductGroup(request):
    serializer = ProductGroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': {"message": "Product group added"}}, status=status.HTTP_201_CREATED)
    return Response({'error': {'code': 422, 'message': 'Validation error', 'error': serializer.errors}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET', 'PATCH', 'DELETE'])
def detailProductGroup(request, pk):
    try:
        product_group = ProductGroup.objects.get(pk=pk)
    except ProductGroup.DoesNotExist:
        return Response({'error': {'code': 404, 'message': 'Not found'}}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductGroupSerializer(product_group)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = ProductGroupSerializer(product_group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': {'code': 422, 'message': 'Validation error', 'error': serializer.errors}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif request.method == 'DELETE':
        product_group.delete()
        return Response({'data': {'message': 'Product group removed'}}, status=status.HTTP_200_OK)


@api_view(['GET'])
def warehouseList(request):
    warehouses = Warehouse.objects.all()
    serializer = WarehouseSerializer(warehouses, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def addWarehouse(request):
    serializer = WarehouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': {"message": "Warehouse added"}}, status=status.HTTP_201_CREATED)
    return Response({'error': {'code': 422, 'message': 'Validation error', 'error': serializer.errors}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET', 'PATCH', 'DELETE'])
def detailWarehouse(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({'error': {'code': 404, 'message': 'Not found'}}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = WarehouseSerializer(warehouse)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = WarehouseSerializer(warehouse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': {'code': 422, 'message': 'Validation error', 'error': serializer.errors}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif request.method == 'DELETE':
        warehouse.delete()
        return Response({'data': {'message': 'Warehouse removed'}}, status=status.HTTP_200_OK)
