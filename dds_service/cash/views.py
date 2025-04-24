from django.shortcuts import render
from rest_framework import viewsets

from cash.models import Status, OperationType, Category, SubCategory, CashFlowRecord
from cash.serializers import StatusSerializer, OperationTypeSerializer, CategorySerializer, SubCategorySerializer, \
    CashFlowRecordSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class OperationTypeViewSet(viewsets.ModelViewSet):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CashFlowRecordViewSet(viewsets.ModelViewSet):
    queryset = CashFlowRecord.objects.all()
    serializer_class = CashFlowRecordSerializer