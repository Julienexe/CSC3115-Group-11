from django.http import request
from django.views.generic import ListView, DetailView
from .models import Program

class ProgramListView(ListView):
    model = Program
    template_name = "program/program_list.html"
    context_object_name = "programs"

class ProgramDetailView(DetailView):
    model = Program
    template_name = "program/program_detail.html"
