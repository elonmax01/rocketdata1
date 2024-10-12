from django.shortcuts import render
from shop.models import Factory, Distributor, Dealer, Retailer, IE, Employee, Product
from shop.serializers import *
from rest_framework import viewsets, permissions
from django.db.models import Avg

# Create your views here.

class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    key = 'admin'
    permission_classes = [permissions.IsAuthenticated]
# URL для поиска по стране: http://127.0.0.1:8000/factory/?country=USA
    def get_queryset(self):
            if self.request.query_params.get('country', None):
                return super().get_queryset().filter(address__country=self.request.query_params.get('country', None))
            else:
                return super().get_queryset() 
        
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer.is_valid(raise_exception=True)
        return super().update(request, *args, **kwargs)
    
    serializer_class = FactorySerializer

class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('country', None):
            return super().get_queryset().filter(address__country=self.request.query_params.get('country', None))
        else:
            return super().get_queryset()
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs) 

    serializer_class = DistributorSerializer



class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('country', None):
            return super().get_queryset().filter(address__country=self.request.query_params.get('country', None))
        else:
            return super().get_queryset()
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    serializer_class = DealerSerializer

class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('country', None):
            return super().get_queryset().filter(address__country=self.request.query_params.get('country', None))
        else:
            return super().get_queryset()
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    serializer_class = RetailerSerializer

class IEViewSet(viewsets.ModelViewSet):
    queryset = IE.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('country', None):
            return super().get_queryset().filter(address__country=self.request.query_params.get('country', None))
        else:
            return super().get_queryset()
        
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    serializer_class = IESerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAunthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    serializer_class = EmployeeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    serializer_class = ProductSerializer

class FactoryStatisticsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    factories_debt = Factory.objects.aggregate(Avg('debt'))['debt__avg']
    distributors_debt = Distributor.objects.aggregate(Avg('debt'))['debt__avg']
    dealers_debt = Dealer.objects.aggregate(Avg('debt'))['debt__avg']
    retailers_debt = Retailer.objects.aggregate(Avg('debt'))['debt__avg']
    ies_debt = IE.objects.aggregate(Avg('debt'))['debt__avg']
    all_debt = factories_debt + distributors_debt + dealers_debt + retailers_debt + ies_debt
    avg_debt = all_debt / 5
    queryset = Factory.objects.filter(debt__gt=avg_debt)

    def get_queryset(self):
        return super().get_queryset()
        
    serializer_class = FactorySerializer

class DistributorStatisticsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    factories_debt = Factory.objects.aggregate(Avg('debt'))['debt__avg']
    distributors_debt = Distributor.objects.aggregate(Avg('debt'))['debt__avg']
    dealers_debt = Dealer.objects.aggregate(Avg('debt'))['debt__avg']
    retailers_debt = Retailer.objects.aggregate(Avg('debt'))['debt__avg']
    ies_debt = IE.objects.aggregate(Avg('debt'))['debt__avg']
    all_debt = factories_debt + distributors_debt + dealers_debt + retailers_debt + ies_debt
    avg_debt = all_debt / 5
    queryset = Distributor.objects.filter(debt__gt=avg_debt)

    def get_queryset(self):
        return super().get_queryset()
        
    serializer_class = DistributorSerializer

class DealerStatisticsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    factories_debt = Factory.objects.aggregate(Avg('debt'))['debt__avg']
    distributors_debt = Distributor.objects.aggregate(Avg('debt'))['debt__avg']
    dealers_debt = Dealer.objects.aggregate(Avg('debt'))['debt__avg']
    retailers_debt = Retailer.objects.aggregate(Avg('debt'))['debt__avg']
    ies_debt = IE.objects.aggregate(Avg('debt'))['debt__avg']
    all_debt = factories_debt + distributors_debt + dealers_debt + retailers_debt + ies_debt
    avg_debt = all_debt / 5
    queryset = Dealer.objects.filter(debt__gt=avg_debt)

    def get_queryset(self):
        return super().get_queryset()
        
    serializer_class = DealerSerializer

class RetailerStatisticsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    factories_debt = Factory.objects.aggregate(Avg('debt'))['debt__avg']
    distributors_debt = Distributor.objects.aggregate(Avg('debt'))['debt__avg']
    dealers_debt = Dealer.objects.aggregate(Avg('debt'))['debt__avg']
    retailers_debt = Retailer.objects.aggregate(Avg('debt'))['debt__avg']
    ies_debt = IE.objects.aggregate(Avg('debt'))['debt__avg']
    all_debt = factories_debt + distributors_debt + dealers_debt + retailers_debt + ies_debt
    avg_debt = all_debt / 5
    queryset = Retailer.objects.filter(debt__gt=avg_debt)

    def get_queryset(self):
        return super().get_queryset()
        
    serializer_class = RetailerSerializer

class IEStatisticsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    factories_debt = Factory.objects.aggregate(Avg('debt'))['debt__avg']
    distributors_debt = Distributor.objects.aggregate(Avg('debt'))['debt__avg']
    dealers_debt = Dealer.objects.aggregate(Avg('debt'))['debt__avg']
    retailers_debt = Retailer.objects.aggregate(Avg('debt'))['debt__avg']
    ies_debt = IE.objects.aggregate(Avg('debt'))['debt__avg']
    all_debt = factories_debt + distributors_debt + dealers_debt + retailers_debt + ies_debt
    avg_debt = all_debt / 5
    queryset = IE.objects.filter(debt__gt=avg_debt)

    def get_queryset(self):
        return super().get_queryset()
        
    serializer_class = IESerializer