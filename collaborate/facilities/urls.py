from django.urls import path
from . import views

app_name = 'facilities'

urlpatterns = [
    path('', views.FacilityListView.as_view(), name='facility-list'),
    path('<int:pk>/', views.FacilityDetailView.as_view(), name='facility-detail'),
    path('service/', views.ServiceListView.as_view(), name='service-list'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment-detail'),
]
