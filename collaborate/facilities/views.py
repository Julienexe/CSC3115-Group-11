from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Facility, Service, Equipment
from .forms import FacilityForm, ServiceForm, EquipmentForm

# Facility Views
class FacilityListView(ListView):
    model = Facility
    template_name = "facilities/facility_list.html"
    context_object_name = "facilities"

class FacilityDetailView(DetailView):
    model = Facility
    template_name = "facilities/facility_detail.html"
    context_object_name = "facility"

class FacilityCreateView(SuccessMessageMixin, CreateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facilities/facility_form.html"
    success_url = reverse_lazy('facilities:facility-list')
    success_message = "Facility '%(name)s' was created successfully"

class FacilityUpdateView(SuccessMessageMixin, UpdateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facilities/facility_form.html"
    success_url = reverse_lazy('facilities:facility-list')
    success_message = "Facility '%(name)s' was updated successfully"

class FacilityDeleteView(SuccessMessageMixin, DeleteView):
    model = Facility
    template_name = "facilities/facility_confirm_delete.html"
    success_url = reverse_lazy('facilities:facility-list')
    success_message = "Facility was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Service Views
class ServiceListView(ListView):
    model = Service
    template_name = "facilities/service_list.html"
    context_object_name = "services"

class ServiceDetailView(DetailView):
    model = Service
    template_name = "facilities/service_detail.html"
    context_object_name = "service"

class ServiceCreateView(SuccessMessageMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "facilities/service_form.html"
    success_url = reverse_lazy('facilities:service-list')
    success_message = "Service '%(name)s' was created successfully"

class ServiceUpdateView(SuccessMessageMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "facilities/service_form.html"
    success_url = reverse_lazy('facilities:service-list')
    success_message = "Service '%(name)s' was updated successfully"

class ServiceDeleteView(SuccessMessageMixin, DeleteView):
    model = Service
    template_name = "facilities/service_confirm_delete.html"
    success_url = reverse_lazy('facilities:service-list')
    success_message = "Service was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Equipment Views
class EquipmentListView(ListView):
    model = Equipment
    template_name = "facilities/equipment_list.html"
    context_object_name = "equipment_list"

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = "facilities/equipment_detail.html"
    context_object_name = "equipment"

class EquipmentCreateView(SuccessMessageMixin, CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = "facilities/equipment_form.html"
    success_url = reverse_lazy('facilities:equipment-list')
    success_message = "Equipment '%(name)s' was created successfully"

class EquipmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = "facilities/equipment_form.html"
    success_url = reverse_lazy('facilities:equipment-list')
    success_message = "Equipment '%(name)s' was updated successfully"

class EquipmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Equipment
    template_name = "facilities/equipment_confirm_delete.html"
    success_url = reverse_lazy('facilities:equipment-list')
    success_message = "Equipment was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)