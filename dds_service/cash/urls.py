from rest_framework.routers import DefaultRouter

from cash.views import StatusViewSet, OperationTypeViewSet, CategoryViewSet, SubCategoryViewSet, CashFlowRecordViewSet

router = DefaultRouter()
router.register(r"status", StatusViewSet)
router.register(r"type", OperationTypeViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"subcategory", SubCategoryViewSet)
router.register(r"cashflow", CashFlowRecordViewSet)

urlpatterns = [] + router.urls