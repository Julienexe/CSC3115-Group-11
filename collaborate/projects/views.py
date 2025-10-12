from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, Outcome

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


