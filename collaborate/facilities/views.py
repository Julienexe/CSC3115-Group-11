from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Facility, Service, Equipment

class FacilityListView(ListView):
    model = Facility
    template_name = "facilities/facility_list.html"
    context_object_name = "facilities"

class FacilityDetailView(DetailView):
    model = Facility
    template_name = "facilities/facility_detail.html"
    context_object_name = "facility"

class ServiceListView(ListView):
    model = Service
    template_name = "facilities/service_list.html"
    context_object_name = "services"

class ServiceDetailView(DetailView):
    model = Service
    template_name = "facilities/service_detail.html"
    context_object_name = "service"

class EquipmentListView(ListView):
    model = Equipment
    template_name = "facilities/equipment_list.html"
    context_object_name = "equipment_list"

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = "facilities/equipment_detail.html"
    context_object_name = "equipment"
