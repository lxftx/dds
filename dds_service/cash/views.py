from drf_yasg.utils import swagger_auto_schema

from cash.models import (CashFlowRecord, Category, OperationType, Status,
                         SubCategory)
from cash.serializers import (CashFlowRecordSerializer, CategorySerializer,
                              OperationTypeSerializer, StatusSerializer,
                              SubCategorySerializer)
from rest_framework import viewsets


class StatusViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющая просматривать или редактировать `статус`."""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class OperationTypeViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющая просматривать или редактировать `типы`."""
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющая просматривать или редактировать `категории`."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющая просматривать или редактировать `подкатегории`."""
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CashFlowRecordViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющая просматривать или редактировать `движение средств`."""
    queryset = CashFlowRecord.objects.all()
    serializer_class = CashFlowRecordSerializer