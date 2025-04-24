from rest_framework import serializers

from .models import (CashFlowRecord, Category, OperationType, Status,
                     SubCategory)


class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationType
        fields = ['id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'operation_type']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']

class CashFlowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlowRecord
        fields = [
            'id',
            'created_at',
            'status',
            'operation_type',
            'category',
            'subcategory',
            'amount',
            'comment',
        ]

    def validate(self, data):
        """Валидация зависимостей между типом, категорией и подкатегорией."""
        category = data.get('category')
        subcategory = data.get('subcategory')
        operation_type = data.get('operation_type')

        if category and category.operation_type != operation_type:
            raise serializers.ValidationError("Категория не соответствует выбранному типу операции.")

        if subcategory and subcategory.category != category:
            raise serializers.ValidationError("Подкатегория не соответствует выбранной категории.")

        return data