from rest_framework import viewsets, filters
from .models import Customer, Product, Employee, TaskBoard
from .serializers import CustomerSerializer, ProductSerializer, EmployeeSerializer, TaskBoardSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TaskBoardViewSet(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'assigned_to__name']
