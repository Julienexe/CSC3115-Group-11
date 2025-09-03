from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Program
from .forms import ProgramForm

class ProgramListView(ListView):
    model = Program
    template_name = "program/program_list.html"
    context_object_name = "programs"

class ProgramDetailView(DetailView):
    model = Program
    template_name = "program/program_detail.html"

class ProgramCreateView(SuccessMessageMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program/program_form.html"
    success_url = reverse_lazy('program:program-list')
    success_message = "Program '%(name)s' was created successfully"

class ProgramUpdateView(SuccessMessageMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program/program_form.html"
    success_url = reverse_lazy('program:program-list')
    success_message = "Program '%(name)s' was updated successfully"

class ProgramDeleteView(SuccessMessageMixin, DeleteView):
    model = Program
    template_name = "program/program_confirm_delete.html"
    success_url = reverse_lazy('program:program-list')
    success_message = "Program was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message)
        return super(ProgramDeleteView, self).delete(request, *args, **kwargs)
