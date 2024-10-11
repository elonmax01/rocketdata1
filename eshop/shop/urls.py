from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'factory', views.FactoryViewSet)
router.register(r'distributor', views.DistributorViewSet)
router.register(r'dealer', views.DealerViewSet)
router.register(r'retailer', views.RetailerViewSet)
router.register(r'ie', views.IEViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'statistics/factory', views.FactoryStatisticsView, basename='statistics1')
router.register(r'statistics/distributor', views.DistributorStatisticsView, basename='statistics2')
router.register(r'statistics/dealer', views.DealerStatisticsView, basename='statistics3')
router.register(r'statistics/retailer', views.RetailerStatisticsView, basename='statistics4')
router.register(r'statistics/ie', views.IEStatisticsView, basename='statistics5')

urlpatterns = [ 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]