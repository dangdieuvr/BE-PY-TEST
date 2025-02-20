from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, EmployeeViewSet, TaskBoardViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskBoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
