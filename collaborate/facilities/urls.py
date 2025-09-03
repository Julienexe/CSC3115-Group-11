from django.urls import path
from . import views

app_name = 'facilities'

urlpatterns = [
    # Facility URLs
    path('', views.FacilityListView.as_view(), name='facility-list'),
    path('create/', views.FacilityCreateView.as_view(), name='facility-create'),
    path('<int:pk>/', views.FacilityDetailView.as_view(), name='facility-detail'),
    path('<int:pk>/update/', views.FacilityUpdateView.as_view(), name='facility-update'),
    path('<int:pk>/delete/', views.FacilityDeleteView.as_view(), name='facility-delete'),

    # Service URLs
    path('service/', views.ServiceListView.as_view(), name='service-list'),
    path('service/create/', views.ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('service/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service-delete'),

    # Equipment URLs
    path('equipment/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/create/', views.EquipmentCreateView.as_view(), name='equipment-create'),
    path('equipment/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:pk>/update/', views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('equipment/<int:pk>/delete/', views.EquipmentDeleteView.as_view(), name='equipment-delete'),
]
