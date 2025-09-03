from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Project, Outcome
from .forms import ProjectForm, OutcomeForm

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

class OutcomeListView(ListView):
    model = Outcome
    template_name = "projects/outcome_list.html"
    context_object_name = "outcomes"

class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = "projects/outcome_detail.html"
    context_object_name = "outcome"

# Project CRUD Views
class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_form.html"
    success_url = reverse_lazy('projects:project-list')
    success_message = "Project '%(title)s' was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_form.html"
    success_message = "Project '%(title)s' was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

    def get_success_url(self):
        return reverse_lazy('projects:project-detail', kwargs={'pk': self.object.pk})

class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = "projects/project_confirm_delete.html"
    success_url = reverse_lazy('projects:project-list')
    success_message = "Project was deleted successfully"

# Outcome CRUD Views
class OutcomeCreateView(SuccessMessageMixin, CreateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = "projects/outcome_form.html"
    success_message = "Outcome '%(title)s' was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def get_success_url(self):
        return reverse_lazy('projects:project-detail', kwargs={'pk': self.object.project.pk})

class OutcomeUpdateView(SuccessMessageMixin, UpdateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = "projects/outcome_form.html"
    success_message = "Outcome '%(title)s' was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

    def get_success_url(self):
        return reverse_lazy('projects:project-detail', kwargs={'pk': self.object.project.pk})

class OutcomeDeleteView(SuccessMessageMixin, DeleteView):
    model = Outcome
    template_name = "projects/outcome_confirm_delete.html"
    success_message = "Outcome was deleted successfully"

    def get_success_url(self):
        return reverse_lazy('projects:project-detail', kwargs={'pk': self.object.project.pk})
