from django.urls import path
from . import views

app_name = 'facilities'

urlpatterns = [
    # Facility URLs
    path('', views.FacilityListView.as_view(), name='facility-list'),
    path('create/', views.FacilityCreateView.as_view(), name='facility-create'),
    path('<uuid:pk>/', views.FacilityDetailView.as_view(), name='facility-detail'),
    path('<uuid:pk>/update/', views.FacilityUpdateView.as_view(), name='facility-update'),
    path('<uuid:pk>/delete/', views.FacilityDeleteView.as_view(), name='facility-delete'),

    # Service URLs
    path('service/', views.ServiceListView.as_view(), name='service-list'),
    path('service/create/', views.ServiceCreateView.as_view(), name='service-create'),
    path('service/<uuid:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('service/<uuid:pk>/update/', views.ServiceUpdateView.as_view(), name='service-update'),
    path('service/<uuid:pk>/delete/', views.ServiceDeleteView.as_view(), name='service-delete'),

    # Equipment URLs
    path('equipment/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/create/', views.EquipmentCreateView.as_view(), name='equipment-create'),
    path('equipment/<uuid:pk>/', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<uuid:pk>/update/', views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('equipment/<uuid:pk>/delete/', views.EquipmentDeleteView.as_view(), name='equipment-delete'),
]